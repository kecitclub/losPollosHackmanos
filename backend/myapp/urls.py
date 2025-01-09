from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    UserRegisterView,
    UserLoginView,
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    
    
]