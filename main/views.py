import os 
import subprocess

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from urllib.parse import urljoin
from .models import Video


def live_player(request):
    return render(request,'main/live.html')

def player(request):
    hls_url = urljoin(settings.MEDIA_URL, 'media/main/output/output.m3u8')
    return render(request, 'main/player.html', {'hls_url': hls_url})

def upload_video(request):
    if request.method == 'POST':
        video = Video(video_file=request.FILES['video_file'], title=request.FILES['video_file'])  # Здесь исправленное место для получения заголовка видео
        video.save()
        encode_video(video.id)
        messages.success(request,'Загрузка завершено успешно')
        return HttpResponseRedirect(reverse('player'))
    return render(request, 'main/index.html')

def encode_video(video_id): 
    video = Video.objects.get(id=video_id)
    video.is_encoding = False
    video.save()
    input_file = video.video_file.path
    output_file = 'media/main/output/output.m3u8'  # Путь к HLS-потоку, исправленный путь
    command = ["ffmpeg",
                "-i", input_file,
                "-c:v", "libx264",
                "-preset", "veryfast",
                "-tune", "zerolatency",
                "-f", "hls",
                "-hls_time", "4",
                "-hls_list_size", "0",
                "-hls_flags", "split_by_time",
                output_file]
    subprocess.run(command)  # Заменил subprocess.Popen на subprocess.run для ожидания завершения процесса
    video.hls_url = 'media/main/output/output.m3u8'  # Исправленный путь
    video.is_encoding = True
    video.save()
