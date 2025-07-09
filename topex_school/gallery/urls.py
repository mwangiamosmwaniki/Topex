from django.urls import path

from topex_school import settings
from . import views
from django.conf.urls.static import static
app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_home, name='gallery_home'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('upload/', views.upload_photo, name='upload_photo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)