from django.db import models


class Post(models.Model):
    userId = models.PositiveIntegerField(blank=True, null=True)
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, default='no title')
    body = models.TextField()

