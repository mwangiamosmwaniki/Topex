from django.contrib import admin
from .models import Album, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ['name', 'created_at']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['album', 'caption', 'uploaded_at']
    list_filter = ['album']
