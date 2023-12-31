from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Product, Comment

class CommentInLine(admin.TabularInline):
    model=Comment
    fields=['author', 'body', 'point_product', 'active']
    extra=1

@admin.register(Product)
class ProductsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display=['tittle', 'price', 'active']
    inlines=[
        CommentInLine,
    ]
    
@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display=['author', 'product', 'body', 'point_product', 'active']

