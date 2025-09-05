from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import MyUser, Item

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
        model = Item
        fields = ['quantity']