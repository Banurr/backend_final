from django.contrib import auth
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


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    rating = models.IntegerField()
    create = models.DateTimeField(auto_now=True)
    modify = models.DateTimeField(auto_now_add=True)
    creator_id = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.text
