from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_user(self, user_name, first_name, last_name, password, **other_fields):

        user_name = self.normalize_email(user_name)
        user = self.model(user_name=user_name, first_name=first_name,
                          last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        return self.create_user(user_name, first_name, last_name, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    user_name = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    objects = CustomAccountManager()
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.user_name
