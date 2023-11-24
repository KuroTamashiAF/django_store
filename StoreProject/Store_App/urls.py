from django.urls import path
from .views import out_order, all_products, find_product, edit_product

urlpatterns = [
    path('client/<int:client_id>/', out_order, name="out_order"),
    path('client/<int:client_id>/<int:num_days_ago>', all_products, name="all_products"),
    path('find_product/', find_product, name="find_product"),
    path('edit_product/<int:product_id>/', edit_product, name="edit_product"),

]
