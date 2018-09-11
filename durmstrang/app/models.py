from django.db import models

from django.contrib.auth.models import User


class Challenge(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=50, null=False, blank=False)
    avatar = models.ImageField(upload_to="images/")
    reached_points = models.IntegerField(default=0, null=False, blank=False)
    expected_points = models.IntegerField(default=0, null=False, blank=False)
    reached_starts = models.IntegerField(default=0, null=False, blank=False)
    expected_starts = models.IntegerField(default=0, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
