from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Order, Client, Product


def out_order(request, client_id):
    client = Client.objects.get(id=client_id)
    order = Order.objects.filter(order_client=client)
    render(request, "Store_App/order_out.html", {"client": client, "order": order})
