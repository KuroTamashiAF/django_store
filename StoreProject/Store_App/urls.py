from django.urls import path
from .views import out_order

urlpatterns = [
    path('client/<int:client_id>/', out_order, name="out_order"),

]
