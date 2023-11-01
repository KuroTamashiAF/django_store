from django.core.management.base import BaseCommand
from Store_App.models import Product


class Command(BaseCommand):
    help = "crete the product"

    def handle(self, *args, **options):
        product = Product(name_product="Microwave Eaton 7500",
                          description_product="Microwave for food",
                          price_product=15489.459,
                          quantity_product=10)
        product.save()
        self.stdout.write(f"{product}")
