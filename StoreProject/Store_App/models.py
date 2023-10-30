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
