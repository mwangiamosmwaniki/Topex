from django.db import models
from django.contrib.auth.models import User

class CalendarEvent(models.Model):
    EVENT_TYPES = [
        ('term', 'Term Start/End'),
        ('exam', 'Exam'),
        ('holiday', 'Holiday'),
        ('deadline', 'Deadline'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
