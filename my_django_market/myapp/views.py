from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import Item

User = get_user_model()

class MainPageView(ListView):
    queryset = Item.objects.all()
    paginate_by = 3
    template_name = 'main.html'
    

class Login(LoginView):
    success_url ='/'
    template_name = 'login.html'

    def get_success_url(self):
        return self.get_success_url
    

class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'

    
class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/'
