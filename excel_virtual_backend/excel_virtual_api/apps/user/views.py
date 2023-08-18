
from django.shortcuts import redirect
import jwt
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .serializers import UserSerializer, ChangePasswordSerializer, RegisterSerializer
from .models import User


# Create your views here.
class UserRegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
class UserVerification(GenericAPIView):
    serializer_class = UserSerializer
    
    def get(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            if not user.is_active:
                user.is_active = True
                user.save()

            return redirect('https://www.google.com/')
        except jwt.ExpiredSignatureError as e:
            return Response({'error': 'Token expried'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as  decodeError:
            return Response({'error': decodeError}, status=status.HTTP_400_BAD_REQUEST)
