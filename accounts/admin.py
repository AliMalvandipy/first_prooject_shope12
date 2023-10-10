from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationFom, CustomUserChangeForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model=CustomUser
    add_form=CustomUserCreationFom
    form=CustomUserChangeForm
    list_display=('username', 'email')
    
