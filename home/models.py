from django.db import models

class Data(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
