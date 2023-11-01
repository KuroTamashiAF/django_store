from django.core.management.base import BaseCommand
from Store_App.models import Product


class Command(BaseCommand):
    help = "out info regarding the name of the products"

    def add_arguments(self, parser):
        parser.add_argument("name")

    def handle(self, *args, **options):
        name_product = options["name"]
        product = Product.objects.filter(name_product__contains=name_product).first()
        self.stdout.write(f"{product}")
