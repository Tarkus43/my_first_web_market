from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import transaction

class MyUser(AbstractUser):
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2, 
        default=10000.00
    )

class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at', ]

    

class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    item = models.ForeignKey('myapp.Item', on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def execute(user: MyUser, item: Item, qty):

        try:
            with transaction.atomic():

                if user.balance < item.price * qty:
                    raise ValueError("Not enough money")
                if item.quantity < qty:
                  raise ValueError("Not enough items")
        
                user.balance -= item.price * qty
                item.quantity -= qty

                user.save()
                item.save()

                
        except Exception as e:
            raise ValueError
        
        return Purchase.objects.create(user=user, item=item, quantity=qty)

    class Meta:
        ordering = ['-created_at', ]

class Refund(models.Model):
    purchase = models.OneToOneField('myapp.Purchase', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at', ]



