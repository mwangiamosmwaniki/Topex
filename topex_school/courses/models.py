from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)  # e.g., Science, Mathematics
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=50, blank=True)  # optional
    fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # optional

    def __str__(self):
        return self.name
