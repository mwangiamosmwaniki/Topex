from django.db import models
from django.contrib.auth.models import User

class LecturerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Added phone number
    profile_picture = models.ImageField(upload_to='lecturer_profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.id_number})"
