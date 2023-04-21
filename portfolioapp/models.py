from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone
from .manager import CustomUserManager
from django.contrib.auth.hashers import mask_hash, make_password

def phone_number_validation(value):
    '''validate phone number'''
    for i in value:
        if i not in "0123456789":
            raise ValidationError("phone_number accepts only integers")
        else:
            return value

class User(AbstractBaseUser, PermissionsMixin):
    '''Table creation for Custom user'''
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=100)
    home_address = models.TextField()
    phone_number = models.CharField(max_length=10, validators=[phone_number_validation])
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["name"]
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username
    

            
    
     
