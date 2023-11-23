from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Order, Client, Product
from datetime import date, timedelta
from .forms import EditProduct


def out_order(request, client_id):
    products = []
    total_price_all = 0
    client = Client.objects.get(id=client_id)
    orders = Order.objects.filter(order_client=client)
    for order in orders:
        products.append(order.order_product)
        total_price_all += order.total_price
    return render(request, "Store_App/order_out.html", {"client": client, "orders": orders,
                                                        "products": products,
                                                        "total_price_all": total_price_all})


def all_products(request, client_id, num_days_ago):
    products = []
    client = Client.objects.get(pk=client_id)
    now = date.today()
    before = now - timedelta(days=num_days_ago)
    orders = Order.objects.filter(order_client=client, date_order__range=(before, now))

    return render(request, "Store_App/out_product_by_days_ago.html",
                  {"before": before, "now": now, "orders": orders, "client": client})


def edit_product(request):
    if request.method == 'POST':
        form = EditProduct(request.POST)
        if form.is_valid():
            id_product = form.cleaned_data['find_product_by_id']
            name_product = form.cleaned_data['name_product']
            description_product = form.cleaned_data['description_product']
            price_product = form.cleaned_data['price_product']
            quantity_product = form.cleaned_data['quantity_product']

            product = Product.objects.get(pk=id_product)
            product.name_product = name_product
            product.description_product = description_product
            product.price_product = price_product
            product.quantity_product = quantity_product
            product.save()
    else:
        form = EditProduct()
    return render(request, '', {'form': form,
                                'product': product})
