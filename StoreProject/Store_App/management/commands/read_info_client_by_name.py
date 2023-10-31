from django.core.management.base import BaseCommand
from Store_App.models import Client


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("name")

    def handle(self, *args, **options):
        name_client = options["name"]
        client = Client.objects.filter(name_client=name_client)
        self.stdout.write(f"{client}")
