from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views.generic.edit import UpdateView
from myapp.forms import MyUserCreationForm, AddItemForm, BuyingForm
from myapp.models import Item, Refund, Purchase

class BuyingView(CreateView):
    http_method_names = ['post']
    form_class = BuyingForm
    success_url = '/'

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs['request'] = self.request
        form_kwargs['pk'] = self.kwargs['pk']
        form_kwargs.pop('instance', None)

        return form_kwargs

    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return redirect('/')
    


class RefundsView(UserPassesTestMixin, ListView):
    model = Refund
    paginate_by = 5
    template_name = 'refunds.html'

    def test_func(self):
        return self.request.user.is_superuser


class EditItemView(UserPassesTestMixin, UpdateView):
    model = Item
    fields = ['name', 'description','price','quantity']
    success_url = '/'
    template_name = 'edit_item.html'

    def test_func(self):
        return self.request.user.is_superuser
    


class AddItemView(UserPassesTestMixin, CreateView):
    form_class = AddItemForm
    template_name = "add_item.html"
    success_url = '/'

    def test_func(self) -> bool:
        return self.request.user.is_superuser


class MainPageView(ListView):
    queryset = Item.objects.all()
    paginate_by = 3
    template_name = 'main.html'
    extra_context ={
        'form': BuyingForm
    }
    

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
