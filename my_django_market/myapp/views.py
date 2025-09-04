from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import MyUserCreationForm
from .models import Item

class MainPageView(ListView):
    queryset = Item.objects.all()
    paginate_by = 3
    template_name = 'main.html'
    

class Login(LoginView):

    template_name = 'login.html'
    redirect_authenticated_user = False
    success_url ='/'
    
    

class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'

    
class Register(CreateView):
    form_class = MyUserCreationForm
    template_name = 'register.html'
    success_url = '/'
