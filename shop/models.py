from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='media/images/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='media/prod/')

    def __str__(self):
        return self.name
