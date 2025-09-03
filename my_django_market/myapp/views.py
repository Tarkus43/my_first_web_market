from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.views import LoginView

class MainPageView(TemplateView):
    paginate_by = 10
    template_name = 'base.html'

class MyLoginView(LoginView):
    pass
