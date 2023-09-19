from pyclbr import Class
from turtle import title
from django.db import models

# Create your models here.

class Article (models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_created=True)
    url = models.URLField(max_length=200)
    body = models.TextField(max_length=10000)
    
def __str__(self):
        return self.title
