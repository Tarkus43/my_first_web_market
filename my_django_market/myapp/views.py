from django.shortcuts import render, redirect 
from django.urls import reverse
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import UpdateView
from django.views import View
from myapp.forms import MyUserCreationForm, AddItemForm, BuyingForm
from myapp.models import Item, Refund
from myapp.transactions import purchase_transaction

class BuyItemView(View):
    http_method_names = ['post'] 
    


    def post(self,request,pk):
        quantity = int(request.POST.get("quantity", 1))
        user_id = self.request.user.id
        
        result = purchase_transaction(pk, quantity, user_id )
        info = result

        if result == 'succes':
            info = 'you succesfuly bought that'
        elif result == 'not enough items':
            info = 'not enough items in storage'
        elif result == 'not enough money':
            info = 'not enough money on your balance'
        else:
            info = 'some other error'
        
        url = reverse("home") + f"?info={result}"
        return redirect(url)

        

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
    extra_context = {'form':BuyingForm}


    

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
