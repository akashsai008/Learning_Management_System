from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, rollno, password=None, **extra_fields):
        """
        Create and return a regular user with a given rollno and password.
        """
        if not rollno:
            raise ValueError('The Roll Number field must be set')
        
        user = self.model(rollno=rollno, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rollno, password=None, **extra_fields):
        """
        Create and return a superuser with a given rollno and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(rollno, password, **extra_fields)


class Lms_Users(AbstractBaseUser, PermissionsMixin):
    rollno = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'rollno'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

