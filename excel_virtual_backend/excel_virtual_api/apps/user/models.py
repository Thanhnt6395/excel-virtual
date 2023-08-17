from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from .manager import CustomUserManager
from utils.choices import GenderChoices

# Create your models here.
class User(AbstractBaseUser):
    id = models.UUIDField(unique=True, auto_created=True, primary_key=True)
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=100, default=None, null=True)
    last_name = models.CharField(max_length=100, default=None, null=True)
    birthday = models.DateField(default=None, null=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.GENDER_IN_CHOICES, default=GenderChoices.OTHER, null=True)
    phone = models.CharField(max_length=20, default=None, null=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'password']
    
    class Meta:
        db_table = 'users'
        
    def __str__(self) -> str:
        return self.email
    