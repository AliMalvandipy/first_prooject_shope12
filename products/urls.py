from django.urls import path

from .views import *

urlpatterns=[
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('comment/<int:product_id>', CommentCreateView.as_view(), name='comment_create'),
]