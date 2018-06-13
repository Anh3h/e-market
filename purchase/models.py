from django.db import models


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

# class UserProduct(models.Model):
#     quantity = models.IntegerField()
#     price = models.FloatField()
#     create_at = models.DateTimeField(auto_now_add=True)
