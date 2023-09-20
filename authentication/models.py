from django.db import models
from django.contrib.auth.models import AbstractUser,_


class Province(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
    

class District(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Phone(models.Model):
    phone_number = models.CharField(null=True)


class Bill(models.Model):
    name = models.CharField()
    pay_amount = models.DecimalField(max_digits=8, decimal_places=2)
    bill_date = models.DateField()


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
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    street_id = models.ForeignKey(Street, on_delete=models.CASCADE, null=True)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True)
    bill_ids = models.ForeignKey(Bill, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

