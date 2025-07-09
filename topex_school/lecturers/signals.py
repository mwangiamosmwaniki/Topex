# lecturers/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import LecturerProfile

@receiver(post_save, sender=User)
def create_lecturer_profile(sender, instance, created, **kwargs):
    if created:
        # Create only if user should be a lecturer (e.g., based on staff status or username prefix)
        LecturerProfile.objects.get_or_create(user=instance)
