from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class UserProfile(models.Model):
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    attribute1 = models.CharField(max_length=100, null=True, blank=True)
    attribute2 = models.CharField(max_length=100, null=True, blank=True)
    attribute3 = models.CharField(max_length=100, null=True, blank=True)