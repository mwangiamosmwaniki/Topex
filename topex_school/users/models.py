from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    # Removed other roles, only 'student' remains
    ROLE_CHOICES = (
        ('student', 'Student'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    bio = models.TextField(blank=True, null=True)
    id_number = models.CharField(
        max_length=30,
        unique=True,
        help_text="Enter full Admission Number e.g. P100/1681/21"
    )

    def __str__(self):
        return f"{self.id_number} - {self.role}"

# Optional utility function for creating student users with profile
def create_user_with_profile(id_number, password):
    username = id_number.replace('/', '_')  # Sanitize for Django username rules
    user = User.objects.create_user(username=username, password=password)
    Profile.objects.create(user=user, id_number=id_number, role='student')
    return user
