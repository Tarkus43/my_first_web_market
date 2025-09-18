from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import MyUser, Item, Purchase
from django import forms
from django.db import transaction

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
        cleaned_data=  super().clean()
        user_qty = cleaned_data['quantity'] 
        item_qty = Item.objects.get(id=self.item_id).quantity
        user_id = self.request.user.id
        user_balance = MyUser.objects.get(id=user_id).balance
        item_price = Item.objects.get(id=self.item_id).price

        if user_balance < item_price:
            self.add_error(None, 'Not enough money')
        if user_qty > item_qty:
            self.add_error(None, 'Not enough items on storage')
        
        self.user = MyUser.objects.get(id=user_id)
        self.item = Item.objects.get(id=self.item_id)
        self.user_quantity = cleaned_data['quantity']
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)


        with transaction.atomic():
            instance.item = self.item
            instance.user = self.user

            self.item.quantity -= self.user_quantity
            self.user.balance -= self.item.price * self.user_quantity
            if commit:
                instance.save()
                self.item.save()
                self.user.save()
                
        return instance

        



    
 