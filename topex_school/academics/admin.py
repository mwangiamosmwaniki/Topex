from django.contrib import admin
from .models import Department, Program, Unit, LectureNote, Message

admin.site.register(Department)
# admin.site.register(Program)
# admin.site.register(Unit)
admin.site.register(LectureNote)

class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'coordinator']

class UnitAdmin(admin.ModelAdmin):
    list_display = ['code', 'title', 'program', 'lecturer']

admin.site.register(Program, ProgramAdmin)
admin.site.register(Unit, UnitAdmin)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'recipient', 'timestamp', 'is_read')
    search_fields = ('subject', 'body', 'sender__username', 'recipient__username')