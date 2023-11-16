from django.core.management.base import BaseCommand
from Store_App.models import Client


class Command(BaseCommand):
    help = "create Client and write him in DB"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="name client")
        parser.add_argument("email", type=str, help="email client")
        parser.add_argument("number_phone", type=str, help="number_phone client")
        parser.add_argument("address_client", type=str, help="address_client client")

    def handle(self, *args, **options):
        name_ = options["name"]
        name = name_.replace("_", " ")
        email_ = options.get("email")
        email = email_.replace("_", " ")
        number_phone_ = options.get("number_phone")
        number_phone = number_phone_.replace("_", " ")
        address_client_ = options.get("address_client")
        address_client = address_client_.replace("_", " ")
        address_client_ = address_client.replace("_", " ")
        address_client = address_client_.replace("_", " ")

        client = Client(name_client=name,
                        email_client=email,
                        number_phone_client=number_phone,
                        address_client=address_client)
        client.save()
