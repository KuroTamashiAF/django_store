from django.core.management.base import BaseCommand
from Store_App.models import Client


class Command(BaseCommand):
    help = "change name client in DB"

    def add_arguments(self, parser):
        parser.add_argument("old_name")
        parser.add_argument("new_name")

    def handle(self, *args, **options):
        new_name = options["new_name"]
        old_name = options["old_name"]
        client = Client.objects.filter(name_client=old_name).first()
        client.name_client = new_name
        client.save()
        self.stdout.write(f"{client}")
