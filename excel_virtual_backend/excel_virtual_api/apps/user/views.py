from django.contrib.auth.hashers import make_password

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer, ChangePasswordSerializer, RegisterSerializer
from utils.send_mail import SendMail


# Create your views here.
class UserRegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()

            username = f"{serializer.validated_data['first_name']} {serializer.validated_data['last_name']}"
            url_verify = 'https://www.google.com/'
            SendMail.send_mail_verify(SendMail, serializer.validated_data['email'], username, url_verify)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
