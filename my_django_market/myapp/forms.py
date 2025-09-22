from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import MyUser, Item, Purchase
from django import forms
from django.db import transaction
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


class BuyingForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.item_id = kwargs.pop('pk', None)
        super().__init__(*args, **kwargs)


    def clean(self):
        cleaned_data = super().clean()
        self.instance.user = self.request.user
        self.instance.item = Item.objects.get(id=self.item_id)
        self.user_quantity = cleaned_data.get('quantity')


        item_qty = self.instance.item.quantity
        user_balance = self.instance.user.balance
        item_price = self.instance.item.price

        if user_balance < item_price:
            self.add_error(None, 'Not enough money')
        if self.user_quantity > item_qty:
            self.add_error(None, 'Not enough items on storage')
        
        return cleaned_data

        



    
 
class BuyingForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)