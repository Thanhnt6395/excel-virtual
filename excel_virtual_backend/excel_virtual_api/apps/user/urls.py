from django.urls import path
from .views import UserRegisterView, UserVerification, VerifyAgain


urlpatterns = [
    path('register', UserRegisterView.as_view()),
    path('verify/<str:token>', UserVerification.as_view()),
    path('verify-again', VerifyAgain.as_view()),
]
