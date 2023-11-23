from django.urls import path
from .views import out_order, all_products, edit_product, find_product

urlpatterns = [
    path('client/<int:client_id>/', out_order, name="out_order"),
    path('client/<int:client_id>/<int:num_days_ago>', all_products, name="all_products"),
    path('find_product/', find_product, name="find_product"),

]
