from django.core.management.base import BaseCommand
from Store_App.models import Client


class Command(BaseCommand):
    help = "change address client in DB"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)
        parser.add_argument("new_address", type=str)

    def handle(self, *args, **options):
        name_client = options["name"]
        new_address = options["new_address"]
        client = Client.objects.filter(name_client=name_client).first()
        client.address_client = new_address
        client.save()
        self.stdout.write(f"{client}")
