from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
class Product(models.Model):
    tittle=models.CharField(max_length=100)
    description=models.TextField()
    price=models.PositiveIntegerField(default=0)
    active=models.BooleanField(default=True)

    datetime_created=models.DateTimeField(auto_now_add=True)
    datetime_modified=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.tittle
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])
    

class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)
    

class Comment(models.Model):
    POINTS=[
        ('1', _('Very bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Prefect')),
    ]


    author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body=models.TextField(verbose_name=_('comment text'))
    point_product=models.CharField(max_length=10, choices=POINTS, verbose_name=_('what is your score?'))

    datetime_created=models.DateTimeField(auto_now_add=True)
    datetime_modified=models.DateTimeField(auto_now=True)

    active=models.BooleanField(default=True)

    #manager
    objects=models.Manager()
    active_comment_manager=ActiveCommentManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
    