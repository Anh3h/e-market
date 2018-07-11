from django.db import models

from custom_profile.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Measurement(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Logistic(models.Model):
    method = models.CharField(max_length=30, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=60, unique=False)
    image_link = models.CharField(max_length=60, unique=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    measurement_id = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    logistic_id = models.ForeignKey(Logistic, on_delete=models.CASCADE)
