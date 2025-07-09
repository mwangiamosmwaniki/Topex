from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'lecturers'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('unit/<int:unit_id>/', views.unit_detail, name='unit_detail'),
    path('upload-materials/', views.upload_materials, name='upload_materials'),
    path('edit-note/<int:pk>/', views.edit_note, name='edit_note'),
    path('delete-note/<int:pk>/', views.delete_note, name='delete_note'),
    path('assigned-units/', views.assigned_units, name='assigned_units'),
    path('messages/', views.Messages, name='messages'),
    path('timetables/', views.timetables, name='timetables'),
    path('login/', views.lecturer_login, name='login'),
    path('logout/', views.lecturer_logout, name='logout'),
    path('assignments/', views.lecturer_assignments, name='lecturer_assignments'),
    path('assignments/<int:assignment_id>/submissions/', views.assignment_submissions, name='assignment_submissions'),
    path('assignments/create/', views.create_assignment, name='create_assignment'),
    path('submissions/<int:submission_id>/grade/', views.grade_submission, name='grade_submission'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
