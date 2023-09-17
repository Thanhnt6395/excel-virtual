
import json
from django.http import HttpResponseRedirect
from django.middleware import csrf
import jwt
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .authenticate import CustomAuthentication

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
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            response = Response()
            tokens = json.loads(serializer.data.get('tokens'))
            response.set_cookie(
				key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
				value = tokens['access_token'],
				expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
				secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
				httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
				samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
			)
            
            response.set_cookie(
				key = 'refresh_token', 
				value = tokens['refresh_token'],
				expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
				secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
				httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
				samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
			)
            csrf.get_token(request)
            response.data = serializer.data
            response.status_code = status.HTTP_200_OK
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserView(GenericAPIView):
    serializer_class = UserSerializer
    
    def get(self, request):
        token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])
        if not token:
            return Response({'detail': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            if not user:
                return Response({'detail': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as e:
            token = request.COOKIES.get('refresh_token')
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            if not user:
                return Response({'detail': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(user)
            response = Response()
            tokens = user.getToken()
            response.set_cookie(
				key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
				value = tokens['access_token'],
				expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
				secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
				httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
				samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
			)
            
            response.set_cookie(
				key = 'refresh_token', 
				value = tokens['refresh_token'],
				expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
				secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
				httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
				samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
			)
            csrf.get_token(request)
            response.data = serializer.data
            response.status_code = status.HTTP_200_OK
            return response
        except jwt.exceptions.DecodeError as  decodeError:
            return Response({'detail': decodeError}, status=status.HTTP_400_BAD_REQUEST)
