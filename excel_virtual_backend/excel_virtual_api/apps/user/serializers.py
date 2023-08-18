from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from utils.choices import GenderChoices
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password

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
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    id = serializers.UUIDField(read_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
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
      
