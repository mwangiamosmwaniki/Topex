from django.urls import path
from django.conf.urls.static import static
from topex_school import settings
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('add/', views.add_event, name='add_event'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)