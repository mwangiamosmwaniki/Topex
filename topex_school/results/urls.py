from django.urls import path
from . import views

app_name = 'results'

urlpatterns = [
    path('add/', views.add_result, name='add_result'),
    path('all/', views.view_results, name='view_results'),
    path('student/<int:applicant_id>/', views.student_results, name='student_results'),
]
