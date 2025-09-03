from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.views import LoginView
from .models import Item

class MainPageView(ListView):
    queryset = Item.objects.all()
    paginate_by = 5
    template_name = 'main.html'
    

class Login(LoginView):
    success_url ='/'
    template_name = 'login.html'

    def get_success_url(self):
        return self.get_success_url
