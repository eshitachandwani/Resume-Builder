from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    profile_name= models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.TextField(max_length=10000)
    city = models.CharField(max_length=100)
    other_info = models.TextField(max_length=10000)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.profile_name

