from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')
    coordinator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='coordinated_programs')

    def __str__(self):
        return f"{self.name} ({self.department.name})"

class Unit(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=200)   
    semester = models.IntegerField(choices=[(1, "Semester 1"), (2, "Semester 2")])
    lecturer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='lectured_units')
    year = models.IntegerField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    enrolled_users = models.ManyToManyField(User, related_name='enrolled_units', blank=True)

    def __str__(self):
        return self.title


class LectureNote(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='notes/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    week = models.PositiveIntegerField(null=True, blank=True)
    topic = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"From {self.sender.username} to {self.recipient.username}: {self.subject}"
    
class Timetable(models.Model):
    # In academics/models.py
    lecturer = models.ForeignKey('lecturers.LecturerProfile', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=50)


class Assignment(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='assignments/', blank=True, null=True)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.unit.code} - {self.title}"

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(default=timezone.now)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.username}"
