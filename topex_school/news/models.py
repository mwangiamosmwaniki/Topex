from django.db import models
from django.contrib.auth.models import User

class NewsPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title
