from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Order, Client, Product
from datetime import date, timedelta
from .forms import EditProduct, FindProduct
import logging

logger = logging.getLogger(__name__)


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
    client = Client.objects.get(pk=client_id)
    now = date.today()
    before = now - timedelta(days=num_days_ago)
    orders = Order.objects.filter(order_client=client, date_order__range=(before, now))

    return render(request, "Store_App/out_product_by_days_ago.html",
                  {"before": before, "now": now, "orders": orders, "client": client})


def find_product(request):
    if request.method == 'POST':
        form = FindProduct(request.POST)
        if form.is_valid():
            product_id = int(form.cleaned_data['product_id'])
            return redirect(to='edit_product', product_id=product_id)
    else:
        form = FindProduct()
    return render(request, 'Store_App/find_product_by_id.html', {'form': form})


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = EditProduct(request.POST)
        if form.is_valid():
            name_product = form.cleaned_data['name_product']
            description_product = form.cleaned_data['description_product']
            price_product = form.cleaned_data['price_product']
            quantity_product = form.cleaned_data['quantity_product']
            # взяли из формы
            logger.info(f'get-{name_product}-{description_product}-{price_product}-{quantity_product}')
            # залогировали
            product.name_product = name_product
            product.description_product = description_product
            product.price_product = price_product
            product.quantity_product = quantity_product
            product.save()
            #внесли в баззу данных



    else:
        form = EditProduct()
    return render(request, 'Store_App/edit_product.html', {'form': form,
                                                           'product': product})
