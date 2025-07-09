from django.contrib import admin
from .models import ContactInfo

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('whatsapp', 'email', 'phone')

admin.site.register(ContactInfo, ContactInfoAdmin)
