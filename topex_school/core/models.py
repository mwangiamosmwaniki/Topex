from django.db import models

class ContactInfo(models.Model):
    whatsapp = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return "Contact Info"
