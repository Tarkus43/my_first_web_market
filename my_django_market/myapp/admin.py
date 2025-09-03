from django.contrib import admin
from .models import MyUser, Item, Purchase, Return
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Item)
admin.site.register(Purchase)
admin.site.register(Return)
