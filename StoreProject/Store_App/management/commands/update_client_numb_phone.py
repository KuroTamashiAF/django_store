from django.core.management.base import BaseCommand
from Store_App.models import Client


class Command(BaseCommand):
    help = "change number phone client in DB"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)
        parser.add_argument("new_phone", type=str)

    def handle(self, *args, **options):
        name_client = options["name"]
        new_phone = options["new_phone"]
        client = Client.objects.filter(name_client=name_client).first()
        client.number_phone_client = new_phone
        client.save()
        self.stdout.write(f"{client}")
