from django.db import models

from custom_profile.models import Profile
from product.models import Product


class Purchase(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=30, unique=True)
    buyer_phone_number = models.CharField(max_length=20, unique=True)
    buyer_location = models.CharField(max_length=20, unique=True)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
