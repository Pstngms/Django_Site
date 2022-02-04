from django.db import models
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    url = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
