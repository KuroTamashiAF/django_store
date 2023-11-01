from django.core.management.base import BaseCommand
from Store_App.models import Product, Order, Client


class Command(BaseCommand):
    help = "create order"

    def handle(self, *args, **options):
        client = Client(name_client="Golum",
                        email_client="misty mountains@Mordor.do",
                        number_phone_client="+668",
                        address_client="misty mountains, cave")
        client.save()
        product = Product(name_product="The Ring of Omnipotence",
                          description_product="One Ring rule all them ",
                          price_product=10000.896,
                          quantity_product=1)
        product.save()
        order = Order(order_client=client,
                      order_product=product,
                      total_price=product.price_product)
        order.save()
