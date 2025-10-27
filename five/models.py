from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    due = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
