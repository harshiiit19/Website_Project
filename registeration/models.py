from django.db import models

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

