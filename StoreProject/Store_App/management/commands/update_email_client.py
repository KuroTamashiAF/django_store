from django.core.management.base import BaseCommand
from Store_App.models import Client


class Command(BaseCommand):
    help = "change email client in DB"

    def add_arguments(self, parser):
        parser.add_argument("name")
        parser.add_argument("new_email")

    def handle(self, *args, **options):
        name_client = options["name"]
        new_email = options["new_email"]
        client = Client.objects.filter(name_client=name_client).first()
        client.email_client = new_email
        client.save()
        self.stdout.write(f"{client}")
