from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import MyUser, Item
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = (UserCreationForm.Meta.fields)

class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description','price','quantity']

class BuyingForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)