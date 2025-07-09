from django.urls import path
from . import views

app_name = 'calendars'
urlpatterns = [
    path('calendar/', views.calendar_home, name='calendar_home'),
    path('add/', views.add_event, name='add_event'),
]
