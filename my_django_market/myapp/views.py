from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import UpdateView
from myapp.forms import MyUserCreationForm, AddItemForm
from myapp.models import Item
from myapp.models import Item

class AddItemView(UserPassesTestMixin, CreateView):
    form_class = AddItemForm
    template_name = "add_item.html"
    success_url = '/'

    def test_func(self) -> bool:
        return self.request.user.username == 'admin'


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
