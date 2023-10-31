from django.core.management.base import BaseCommand
from Store_App.models import Client


class Command(BaseCommand):
    help = "change email client in DB"

    def add_arguments(self, parser):
        parser.add_argument("old_email")
        parser.add_argument("new_email")

    def handle(self, *args, **options):
        new_email = options["new_email"]
        old_email = options["old_email"]
        client = Client.objects.filter(email_client=old_email).first()
        client.email_client = new_email
        client.save()
        self.stdout.write(f"{client}")
