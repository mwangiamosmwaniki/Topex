from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    SEMESTER_CHOICES = [
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES, blank=True, null=True)  # ✅ Add this


class FeeStructure(models.Model):
    program = models.CharField(max_length=100)
    semester = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class BillingStatement(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_paid = models.BooleanField(default=False)

class Payment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    receipt_number = models.CharField(max_length=100)

class SemesterRegistration(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    registered_on = models.DateTimeField(auto_now_add=True)

class Transcript(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.CharField(max_length=100)
    grade = models.CharField(max_length=5)
    semester = models.CharField(max_length=10)
