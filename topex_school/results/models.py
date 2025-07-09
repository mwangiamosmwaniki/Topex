from django.db import models
from admissions.models import Applicant, Course

class Result(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    unit_name = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2)
    semester = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=9)
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.full_name()} - {self.unit_name} ({self.grade})"
