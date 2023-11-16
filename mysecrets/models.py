from django.db import models


class Secret(models.Model):
    secret_text = models.TextField()
    unique_url = models.CharField(max_length=100, unique=True)
    views_remaining = models.IntegerField(default=1)
