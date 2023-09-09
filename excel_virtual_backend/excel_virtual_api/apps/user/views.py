
from django.http import HttpResponseRedirect
import jwt
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .serializers import LoginSerializer, UserSerializer, ChangePasswordSerializer, RegisterSerializer, VerifyAgainSerializer
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
                return HttpResponseRedirect(redirect_to=f'http://localhost:5173/verify/{token}/notFound')
            if not user.is_active:
                user.is_active = True
                user.save()

            return HttpResponseRedirect(redirect_to=f'http://localhost:5173/verify/{token}/success')
        except jwt.ExpiredSignatureError as e:
            return HttpResponseRedirect(redirect_to=f'http://localhost:5173/verify/{token}/expired')
        except jwt.exceptions.DecodeError as  decodeError:
            return HttpResponseRedirect(redirect_to=f'http://localhost:5173/verify/{token}/decode')
          
          
class VerifyAgain(GenericAPIView):
    serializer_class = VerifyAgainSerializer
    
    def post(self, request):
        serializer = VerifyAgainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            
            response = Response(data, status=status.HTTP_200_OK)
            token = {
                'access_token': serializer.data.get('access_token'),
                'refresh_token': serializer.data.get('refresh_token'),
            }
            response.set_cookie(key='jwt', value=token, httponly=True)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
