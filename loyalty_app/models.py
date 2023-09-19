from django.db import models



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


class Customer(models.Model):
    name = models.CharField(max_length=200)
    total_point = models.IntegerField(default=0)
    accumulate_point = models.IntegerField(default=0)
    bonus_point = models.IntegerField(default=0)
    start_time = models.DateField()
    bday = models.DateField("Birth day")
    identify_card = models.CharField()
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    street_id = models.ForeignKey(Street, on_delete=models.CASCADE, null=True)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True)
    bill_ids = models.ForeignKey(Bill, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField('Point exchange', default=0)
    cantidad = models.IntegerField()
    expired_time = models.DateTimeField()
    cart = models.ManyToManyField(Cart)

    def __str__(self):
        return f'{self.name} can be exchanged with {self.price}, it will expired at {self.expired_time}'


class Category(models.Model):
    name = models.CharField(max_length=200)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
