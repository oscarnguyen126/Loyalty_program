from django.db import models
from authentication.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField("Point exchange", default=0)
    expired_time = models.DateField(default=1)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} can be exchanged with {self.price}"
