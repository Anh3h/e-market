from django.db import models

from custom_profile.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Measurement(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Products(models.Model):
    name = models.CharField(max_length=30, unique=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    measurement_id = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='products')


class Logistic(models.Model):
    method = models.CharField(max_length=30, unique=True)


class UserProduct(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    logistic_id = models.ForeignKey(Logistic, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
