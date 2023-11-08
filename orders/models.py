from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'))
    is_paid=models.BooleanField(_('is paid?'),default=False)
    

    first_name=models.CharField(_('first name'),max_length=200)
    last_name=models.CharField(_('last name'),max_length=200)
    phone_number=models.CharField(_('phone number'),max_length=15)
    address=models.CharField(_('address'),max_length=700)
    order_notes=models.CharField(_('order notes'),max_length=700, blank=True)


    datetime_created=models.DateTimeField(_('created'),auto_now_add=True)
    datetime_modified=models.DateTimeField(_('modified'),auto_now=True)

    def __str__(self):
        return f'order:{self.id}'


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey('products.Product', on_delete=models.CASCADE,related_name='order_item')
    quantity=models.PositiveBigIntegerField(default=1)
    price=models.PositiveBigIntegerField()

    def __str__(self):
        return f'OrderItem {self.id}:{self.product} *  {self.quantity} price:{self.price}'

