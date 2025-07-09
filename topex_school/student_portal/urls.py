from django.urls import path
from . import views

app_name = 'student_portal'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('payments/', views.payment_history, name='payment_history'),
    path('fee-structure/', views.fee_structure, name='fee_structure'),
    path('register/', views.semester_registration, name='semester_registration'),
    path('transcript/', views.transcript, name='transcript'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.student_login, name='login'),
    path('logout/', views.student_logout, name='logout'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]

