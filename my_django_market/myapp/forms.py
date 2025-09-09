from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
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
    qty = forms.IntegerField(min_value=1, required=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.item_id = kwargs.pop('pk', None)
        super().__init__(*args, **kwargs)
    
    def clean_qty(self):
        user_qty = self.cleaned_data['qty']
        item_qty = Item.objects.get(id=self.item_id).quantity

        if user_qty > item_qty:
            raise ValidationError('Not enough items on storage')
        
    def clean_balance(self):
        user_id = self.request.user.id
        user_balance = MyUser.objects.get(id=user_id).balance
        item_price = Item.objects.get(id=self.item_id).price

        if user_balance < item_price:
            raise ValidationError('Not enough money on balance')
        

    def clean(self):
        cleaned_data =  super().clean()
        user_qty = cleaned_data['qty']
        item_qty = Item.objects.get(id=self.item_id).quantity
        user_id = self.request.user.id
        user_balance = MyUser.objects.get(id=user_id).balance
        item_price = Item.objects.get(id=self.item_id).price

        



    
 