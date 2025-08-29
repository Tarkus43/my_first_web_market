from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser

class MyUser(AbstractUser):
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2, 
        default=0.00
    )

class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)

class Purchase(models.Model):
    user = models.ForeignKey("myapp.User", on_delete=models.DO_NOTHING)
    item = models.ForeignKey('myapp.Item', on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(null=False, blank=False)


