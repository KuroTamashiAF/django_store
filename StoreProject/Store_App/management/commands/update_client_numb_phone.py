from django.core.management.base import BaseCommand
from Store_App.models import Client


class Command(BaseCommand):
    help = "change number phone client in DB"

    def add_arguments(self, parser):
        parser.add_argument("old_phone", type=str)
        parser.add_argument("new_phone", type=str)

    def handle(self, *args, **options):
        new_phone = options["new_phone"]
        old_phone = options["old_phone"]
        client = Client.objects.filter(number_phone_client=old_phone).first()
        client.number_phone_client = new_phone
        client.save()
        self.stdout.write(f"{client}")
