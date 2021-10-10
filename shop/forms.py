from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import Order

class Orderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'address', 'city', 'state', 'zipcode']