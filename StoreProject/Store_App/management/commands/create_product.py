from django.core.management.base import BaseCommand
from Store_App.models import Product


class Command(BaseCommand):
    help = "crete the product"

    def handle(self, *args, **options):
        product = Product(name_product="NoteBook Lenovo gaming-3",
                          description_product="NoteBook",
                          price_product=95000.00,
                          quantity_product=5)
        product.save()
        self.stdout.write(f"{product}")
