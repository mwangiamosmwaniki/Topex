from django.contrib import admin
from .models import NewsPost

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted']
    search_fields = ['title', 'content']
    list_filter = ['date_posted']
