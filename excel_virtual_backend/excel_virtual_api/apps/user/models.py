import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

from .manager import CustomUserManager
from utils.choices import GenderChoices

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=100, default=None, null=True)
    last_name = models.CharField(max_length=100, default=None, null=True)
    birthday = models.DateField(default=None, null=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.GENDER_IN_CHOICES, default=GenderChoices.OTHER, null=True)
    phone = models.CharField(max_length=20, default=None, null=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'users'
        
    def __str__(self) -> str:
        return self.email
    
    def getToken(self):
        token = RefreshToken.for_user(self)
        return {
			"access_token": str(token.access_token),
			"refresh_token": str(token)
		}
        
    def getUsername(self):
        return f"{self.first_name if self.first_name else ''} {self.last_name if self.last_name else ''}"
    