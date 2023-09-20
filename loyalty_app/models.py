from django.db import models
from authentication.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField('Point exchange', default=0)
    cantidad = models.IntegerField()
    expired_time = models.DateTimeField()

    def __str__(self):
        return f'{self.name} can be exchanged with {self.price}, it will expired at {self.expired_time}'


class Category(models.Model):
    name = models.CharField(max_length=200)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
