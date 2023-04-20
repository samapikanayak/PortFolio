from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username,name, password, **other_fields):
        if not email:
            raise ValueError(_("you must provide a email"))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get("is_staff") is not True:
            raise ValueError("superuser must be assigned to is_staff=True")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("superuser must be assigned to is_superuser=True")
        return self.create_user(email, username, name, password, **other_fields)