from django.shortcuts import render
from django.views.generic import ListView, TemplateView

class MainPageView(TemplateView):
    paginate_by = 10
    template_name = 'base.html'
