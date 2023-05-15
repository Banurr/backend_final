from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='categ/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    amount = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='prod/')

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True)
    money = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

