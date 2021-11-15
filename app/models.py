from django.db import models
from django.conf import settings

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class Network(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Show(models.Model):
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.PROTECT, null=True)
    network = models.ForeignKey(Network, on_delete=models.PROTECT, null=True)
    show = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.show