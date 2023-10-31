from django.core.management.base import BaseCommand
from Store_App.models import Client


class Command(BaseCommand):
    help = "out all clients from DB"

    def handle(self, *args, **options):
        clients = Client.objects.all()
        self.stdout.write(f"{clients}")
