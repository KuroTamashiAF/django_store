from django.core.management.base import BaseCommand
from Store_App.models import Client


class Command(BaseCommand):
    help = "find client by name_client from DB"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help='name_client')

    def handle(self, *args, **options):
        name = options["name"]
        client = Client.objects.filter(name_client=name).first()
        self.stdout.write(f"{client}")
