from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('add/', views.add_news, name='add_news'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

