from django.db import models
from django.contrib.auth.models import User


class UserInterest(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


# Create your models here.
class UserProfile(models.Model):
    # owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # details
    address = models.CharField(max_length=500, blank=True, null=True)
    interests = models.ManyToManyField(UserInterest, blank=True)
