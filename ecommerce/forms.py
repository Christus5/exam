from django import forms

from ecommerce.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('ticket',)
