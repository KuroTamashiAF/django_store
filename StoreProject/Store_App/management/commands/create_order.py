from django.core.management.base import BaseCommand
from Store_App.models import Product, Order, Client


class Command(BaseCommand):
    help = "create order"

    def add_arguments(self, parser):
        parser.add_argument("order_client", type=int, help="id client")
        parser.add_argument("order_product", type=int, help="id product")

    def handle(self, *args, **options):
        id_client = options.get("order_client")
        client = Client.objects.get(pk=id_client)

        id_product = options.get("order_product")
        product = Product.objects.get(pk=id_product)

        total_price = product.price_product

        order = Order(order_client=client,
                      order_product=product,
                      total_price=total_price)
        order.save()
