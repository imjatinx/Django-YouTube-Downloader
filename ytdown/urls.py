from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='youtube'),
    path('download/', views.download_video, name='download_video'),
    # Include a new URL pattern with a parameter
    path('download/<str:videoUrl>/', views.download_video, name='download_video_with_param'),

]
