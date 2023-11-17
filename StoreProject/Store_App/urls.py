from django.urls import path
from .views import out_order, all_products

urlpatterns = [
    path('client/<int:client_id>/', out_order, name="out_order"),
    path('client/<int:client_id>/<int:num_days_ago>', all_products, name="all_products"),

]
