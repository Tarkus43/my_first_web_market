from django.db import transaction
from myapp.models import Item, Purchase, MyUser


def purchase_transaction(item_id, item_qty, user_id) -> str:
    try:
        with transaction.atomic():
            
            item = Item.objects.get(id=item_id)
            user = MyUser.objects.get(id=user_id)

            if item.quantity < item_qty:
                return 'not enough items'
            
            if user.balance < item.price * item_qty:
                return 'not enough money'

            item.quantity -= item_qty
            item.save()
            user.balance -= item.price * item_qty
            user.save()
            purchase = Purchase(user=user, item=item, quantity=item_qty)
            purchase.save()
            
            return 'succes'
    except Exception:
        return 'error'

