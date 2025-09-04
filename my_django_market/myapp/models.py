from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    item = models.OneToOneField('myapp.Item', on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', ]

class Return(models.Model):
    purchase = models.OneToOneField('myapp.Purchase', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at', ]



