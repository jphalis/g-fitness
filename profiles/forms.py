from django import forms
from django.contrib.auth.models import User

from .models import UserAddress


class UserAddressForm(forms.ModelForm):
    default = forms.BooleanField(label='Default Shipping', required=False)
    default1 = forms.BooleanField(label='Default Billing', required=False)

    class Meta:
        model = UserAddress
        fields = ['name', 'address', 'address2', 'city', 'state',
                  'zipcode', 'phone']


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=30, required=True)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=30, required=True)
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=75, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
