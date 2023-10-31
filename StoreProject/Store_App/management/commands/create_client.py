from django.core.management.base import BaseCommand
from Store_App.models import Client


class Command(BaseCommand):
    help = "create Client and write him in DB"

    def handle(self, *args, **options):
        client = Client(name_client="Alex", email_client="sofa@mouse.net",
                        number_phone_client="+39264564563",
                        address_client="island,Paradise,from,AoT")
        client.save()

