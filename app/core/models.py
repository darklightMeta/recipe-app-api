"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """
    Custom user manager.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a new user.
        """
        if not email:
            raise ValueError('Users must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)  # set_password is required by Django
        user.save(using=self._db)  # using=self._db is required by Django

        return user

    def create_superuser(self, email, password):
        """
        Create and save a new superuser.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that supports using email instead of username.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # required by Django
    is_staff = models.BooleanField(default=False)  # required by Django

    objects = UserManager()

    USERNAME_FIELD = 'email'  # USERNAME_FIELD is required by Django

    def __str__(self):
        """
        Return string representation of user.
        """
        return self.email
