from django.db import models
from django.utils import timezone


# Create your models here.
class GhostPost(models.Model):
    boast_or_roast = models.BooleanField(default=False)
    post = models.CharField(max_length=500)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=timezone.now)
