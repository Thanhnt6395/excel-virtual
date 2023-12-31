import json
from django.conf import settings
import jwt, datetime
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import AuthenticationFailed
from utils.choices import GenderChoices
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import check_password

from .models import User
from utils.send_mail import SendMail
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, min_length=8)
    first_name = serializers.CharField(max_length=50, required=False)
    last_name = serializers.CharField(max_length=50, required=False)
    id = serializers.UUIDField(read_only=True)

    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
            username = f"{user.first_name} {user.last_name}"
            token = RefreshToken.for_user(user).access_token
            SendMail.send_mail_verify(SendMail, user.email, username, str(token))
        except Exception as e:
            raise e
        return user



class UserUpdateSerializer(serializers.Serializer):
    id = serializers.UUIDField(format='hex')
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    birthday = serializers.DateField(required=False)
    gender = serializers.ChoiceField(choices=GenderChoices.GENDER_IN_CHOICES, default=GenderChoices.OTHER)
    phone = serializers.CharField(required=False)
    is_active = serializers.BooleanField(default=False, required=False)
    is_superuser = serializers.BooleanField(default=False, required=False)

        
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance
    

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)

    def update(self, instance, validated_data):
        password = validated_data.get('password', instance.password)
        instance.set_password(password)
        instance.save()
        return instance
      
class VerifyAgainSerializer(serializers.Serializer):
    token = serializers.CharField()
    
    def create(self, validated_data):
        try:
            payload = jwt.decode(validated_data.get('token'), settings.SECRET_KEY, options={"verify_exp": False}, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            username = f"{user.first_name if user.first_name else ''} {user.last_name if user.last_name else ''}"
            token = RefreshToken.for_user(user).access_token
            SendMail.send_mail_verify(SendMail, user.email, username, str(token))
        except Exception as e:
            raise e
        return token
      

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, min_length=8)
    tokens = serializers.CharField(read_only=True, max_length=255)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = User.objects.get(email=email)
        if not user:
            raise AuthenticationFailed('User not found!')
        if not user.is_active:
            raise AuthenticationFailed("User hasn't activated yet!")
        if not check_password(password, user.password):
            raise AuthenticationFailed('Password incorrect!')
        return {
          "email": user.email,
          "username": user.getUsername(),
          "tokens": json.dumps(user.getToken())
        }
