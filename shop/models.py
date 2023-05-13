from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField()
