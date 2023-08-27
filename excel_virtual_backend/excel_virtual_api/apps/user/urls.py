from django.urls import path
from .views import UserRegisterView, UserVerification


urlpatterns = [
    path('register', UserRegisterView.as_view()),
    path('verify/<str:token>', UserVerification.as_view()),
]
