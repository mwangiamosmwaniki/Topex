from django.urls import path
from . import views

app_name = 'admissions'

urlpatterns = [
    path('dashboard/<int:applicant_id>/', views.dashboard, name='dashboard'),
    path('apply/', views.apply, name='apply'),
    path('success/', views.success, name='success'),
]
