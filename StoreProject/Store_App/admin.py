from django.contrib import admin
from .models import Client, Product, Order
from django.utils.html import format_html


class AdminClient(admin.ModelAdmin):
    """Настройка для отображения всех клинтов список """
    list_display = ['id', 'name_client', 'email_client', 'number_phone_client', 'date_registrations_client']
    ordering = ['id']
    list_filter = ['date_registrations_client', 'number_phone_client']
    search_fields = ['name_client', 'email_client', 'number_phone_client']
    search_help_text = 'Поиск производится по полям "name_client, "email_client","number_phone_client"'

    """Настройка объекта """

    readonly_fields = ['date_registrations_client']


class AdminProduct(admin.ModelAdmin):
    """Настройка для отображения всех продуктов список """
    list_display = ['id', 'name_product', 'quantity_product', 'price_product', 'date_registrations_product',
                    'image_preview']
    ordering = ['id']
    list_filter = ['price_product', 'date_registrations_product']
    search_fields = ['name_product', 'description_product']
    search_help_text = "Поиск по полю Имя и Описание "

    """Настройка объекта """
    fields = ['id', 'name_product', 'description_product', 'price_product', 'quantity_product',
              'date_registrations_product', 'image_preview', 'fotografy_product']
    readonly_fields = ['id', 'date_registrations_product', 'image_preview', ]

    def image_preview(self, obj):
        if obj.fotografy_product:
            if isinstance(obj.fotografy_product, str):
                return "No image"
            return format_html(f'<img src="{obj.fotografy_product.url}"width="50" heigth="50" />')
        return "No image"

    image_preview.short_description = "Image preview"


class AdminOrder(admin.ModelAdmin):
    """Настройка для отображения всех заказов список """
    list_display = ['id', 'order_client', 'order_product', 'total_price', 'date_order']
    ordering = ['id']
    list_filter = ['date_order']
    search_fields = ['id']
    search_help_text = "Поиск по полю id"
    """Настройка вывода информации об объекте"""
    fields = ['id', 'order_client', 'order_product', 'total_price', 'date_order']
    readonly_fields = ['id', 'date_order']


admin.site.register(Client, AdminClient)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
