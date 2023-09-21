from django.db import models
from django.contrib.auth.models import AbstractUser, _
from phone_field import PhoneField


class Province(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField()
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField()
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(_("username"), max_length=200, unique=True)
    password = models.CharField(_("password"))
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    total_point = models.IntegerField(default=0)
    accumulate_point = models.IntegerField(default=0)
    bonus_point = models.IntegerField(default=0)
    start_time = models.DateField(auto_now=True)
    bday = models.DateField("Birth day")
    identify_card = models.IntegerField()
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, null=True)
    phone = PhoneField(null=True, unique=True)
    mobile = PhoneField(null=True, unique=True)

    def __str__(self):
        return self.name


class Bill(models.Model):
    name = models.CharField()
    pay_amount = models.DecimalField(max_digits=8, decimal_places=2)
    bill_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
