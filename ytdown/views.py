from django.shortcuts import render, redirect
from pytube import YouTube
import datetime
import requests
from django.http import StreamingHttpResponse
from django.contrib import messages
from django.http import JsonResponse
import pytube


# def youtube(request):
#     if request.method == 'POST':
#         url = request.POST.get('url')
#         yt = YouTube(url)
#         try:
#             streamList = yt.streams

#             # for stream in streamList:
#             #     print(stream)

#             # p = streamList.get_by_itag(137)
#             # p.download()
#             # print(p)
#             # print(p.filesize_mb)

#             context = {
#                 'title': yt.title,
#                 'thumbnail': yt.thumbnail_url,
#                 'duration': str(datetime.timedelta(seconds=yt.length)),

#                 'audioStreams': streamList.filter(only_audio=True),
#                 'progressiveStreams': streamList.filter(progressive=True),
#             }

#             return render(request, 'ytdown/home.html', {'context': context})
#         except:
#             messages.error(request, 'Chala ja bsdk. galat link daali hai.')
#             return render(request, 'ytdown/home.html')

#     return render(request, 'ytdown/home.html')


# def download_proxy(request, file_url, filename):
#     response = requests.get(file_url, stream=True)

#     # Set the Content-Disposition header to force download
#     response_headers = {
#         'Content-Disposition': f'attachment; filename="{filename}"', }

#     print('response==>', response.headers)


#     # Return the response as a streaming response
#     return StreamingHttpResponse(
#         response.iter_content(chunk_size=4096),
#         content_type='video/mp4',
#         status=response.status_code,
#         reason=response.reason,
#         headers=response_headers
#     )


def index(request):
    return render(request, 'ytdown/index.html')

def download_video(request):
    if request.method == 'GET':
        video_url = request.GET.get('videoUrl')
        if video_url:
            try:
                yt = pytube.YouTube(video_url)
                video = yt.streams.get_highest_resolution()
                download_link = video.url
                return JsonResponse({'downloadLink': download_link})
            except Exception as e:
                return JsonResponse({'error': str(e)})
    
    return JsonResponse({'error': 'Invalid request.'})