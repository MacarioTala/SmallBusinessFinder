"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Restaurant

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class SubmitRestaurantForm(forms.Form):
    restaurant_name= forms.CharField(max_length=100,required=False)
    restaurant_address= forms.CharField(max_length=100,required=False)
    #class Meta:
    #    model = Restaurant
    #    fields =['name','address']