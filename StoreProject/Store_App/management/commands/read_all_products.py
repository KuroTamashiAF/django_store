from django.core.management.base import BaseCommand
from Store_App.models import Product


class Command(BaseCommand):
    help = "out all products in DB"

    def handle(self, *args, **options):
        products = Product.objects.all()
        self.stdout.write(f"{products}")
