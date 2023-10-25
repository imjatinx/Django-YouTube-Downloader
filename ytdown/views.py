from django.shortcuts import render, redirect, HttpResponse
from pytube import YouTube
import datetime
import requests
from django.http import StreamingHttpResponse
from django.contrib import messages
from django.http import JsonResponse
import pytube

def index(request):
    return render(request, 'ytdown/youtube.html')

def download_video(request):
    if request.method == 'GET':
        video_url = request.GET.get('videoUrl')
        if video_url:
            try:
                yt = pytube.YouTube(video_url)
                video = yt.streams.get_highest_resolution()
                download_link = video.url

                response = requests.get(download_link, stream=True)

                # Set the Content-Disposition header to force download
                response_headers = {
                    'Content-Disposition': f'attachment; filename="{yt.title}.mp4"', }

                # return JsonResponse({'downloadLink': download_link})
                return StreamingHttpResponse(
                    response.iter_content(chunk_size=4096),
                    content_type='video/mp4',
                    status=response.status_code,
                    reason=response.reason,
                    headers=response_headers
                )
            except Exception as e:
                return JsonResponse({'error': str(e)})
    
    return JsonResponse({'error': 'Invalid request.'})
