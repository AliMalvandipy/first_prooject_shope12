from django.urls import path

from . import views

urlpatterns=[
    path('', views.HomePage.as_view(), name='home'),
    path('aboutus/', views.AboutUs.as_view(), name='aboutus'),
]