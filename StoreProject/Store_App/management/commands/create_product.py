from django.core.management.base import BaseCommand
from Store_App.models import Product



class Command(BaseCommand):
    help = "crete the product"

    def add_arguments(self, parser):
        parser.add_argument("name_product", type=str)
        parser.add_argument("description_product", type=str)
        parser.add_argument("price_product", type=float)
        parser.add_argument("quantity_product", type=int)

    def handle(self, *args, **options):
        name_product = options["name_product"].replace("_", " ")
        description_product = options["description_product"].replace("_", " ")
        price_product = options["price_product"]
        quantity_product = options["quantity_product"]

        product = Product(name_product=name_product,
                          description_product=description_product,
                          price_product=price_product,
                          quantity_product=quantity_product)
        product.save()
        self.stdout.write(f"{product}")
