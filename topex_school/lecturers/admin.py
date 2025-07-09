from django.contrib import admin
from .models import LecturerProfile

@admin.register(LecturerProfile)
class LecturerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id_number', 'department', 'phone_number', 'profile_picture')
    search_fields = ('user__username', 'id_number', 'department', 'phone_number')
