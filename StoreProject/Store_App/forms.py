from django import forms


class FindProduct(forms.Form):
    find_product_by_id = forms.IntegerField()


class EditProduct(forms.Form):
    name_product = forms.CharField(min_length=1, max_length=50)
    description_product = forms.CharField(min_length=1, max_length=50)
    price_product = forms.DecimalField(max_digits=7, decimal_places=2)
    quantity_product = forms.IntegerField()
