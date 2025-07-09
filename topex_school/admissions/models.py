from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    ]
    status = models.CharField(max_length=1, choices=status_choices, default='P')

    def __str__(self):
        return f"{self.applicant} - {self.course} ({self.get_status_display()})"
