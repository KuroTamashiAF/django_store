from django.db import models


class Client(models.Model):
    name_client = models.CharField(max_length=100)
    email_client = models.EmailField()
    number_phone_client = models.CharField(max_length=13)
    address_client = models.CharField(max_length=100)
    date_registrations_client = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.name_client}"


class Product(models.Model):
    name_product = models.CharField(max_length=100)
    description_product = models.TextField()
    price_product = models.DecimalField(max_digits=7, decimal_places=2)
    quantity_product = models.IntegerField()
    date_registrations_product = models.DateField(auto_now_add=True)
    fotografy_product = models.ImageField()

    def __str__(self):
        return f"{self.name_product}"


class Order(models.Model):
    order_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    date_order = models.DateField(auto_now_add=True)
