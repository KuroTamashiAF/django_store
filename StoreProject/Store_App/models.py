from django.db import models


class Client(models.Model):
    name_client = models.CharField(max_length=100)
    email_client = models.EmailField()
    number_phone_client = models.CharField(max_length=13)
    address_client = models.CharField(max_length=100)
    date_registrations_client = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"{self.name_client} {self.number_phone_client} {self.email_client} {self.address_client}"
                f"{self.date_registrations_client}")


class Product(models.Model):
    name_product = models.CharField(max_length=100)
    description_product = models.TextField()
    price_product = models.DecimalField(max_digits=7, decimal_places=2)
    quantity_product = models.IntegerField()
    date_registrations_product = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"{self.name_product} {self.price_product} {self.date_registrations_product} "
                f"{self.quantity_product}")
