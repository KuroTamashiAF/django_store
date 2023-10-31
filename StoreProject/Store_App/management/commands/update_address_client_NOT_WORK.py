from django.core.management.base import BaseCommand
from Store_App.models import Client


class Command(BaseCommand):
    help = "change address client in DB"

    def add_arguments(self, parser):
        parser.add_argument("old_address", type=str)
        parser.add_argument("new_address", type=str)

    def handle(self, *args, **options):
        new_address = options["new_address"]
        old_address = options["old_address"]
        client = Client.objects.filter(address_client=old_address).first()
        client.address_client = new_address
        client.save()
        self.stdout.write(f"{client}")


"""client.address_client = new_address
    ^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'address_client'"""

"""
from StoreProject.Store_App.models import Client
ModuleNotFoundError: No module named 'StoreProject.Store_App'
(venv) PS E:\Python_projects\django\Store\StoreProject> 
"""
