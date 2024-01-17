from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import player,live_player,upload_video

urlpatterns = [
    path('', upload_video, name = 'index'),
    path('player/', player, name = 'player'),
    path('live/', live_player, name = 'live')
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)