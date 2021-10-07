from django.db import models

# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profilepic", null=True, blank=True)
    caption = models.TextField()