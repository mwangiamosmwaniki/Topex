from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact_view, name='contact'),
    path('E-learning/', views.student_dashboard, name='student_dashboard'),
    path('lecturer/dashboard/', views.lecturer_dashboard, name='lecturer_dashboard'),
    path('assignments/', views.available_assignments, name='available_assignments'),
    path('assignments/<int:assignment_id>/submit/', views.submit_assignment, name='submit_assignment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
