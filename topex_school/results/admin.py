from django.contrib import admin
from .models import Result

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'course', 'unit_name', 'score', 'grade', 'semester', 'academic_year', 'date_recorded']
    search_fields = ['applicant__first_name', 'applicant__last_name', 'unit_name']
