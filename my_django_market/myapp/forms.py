from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.meta):
        model = MyUser
        fields = (UserCreationForm.fields)