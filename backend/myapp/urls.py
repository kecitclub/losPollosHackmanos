from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    UserRegisterView,
    UserLoginView,
    UserProfileUpdateView,
    ProfileFilterView
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('user-profile/<str:username>/', UserProfileUpdateView.as_view(), name='user-profile'),
    path('profiles/', ProfileFilterView.as_view(), name='profile-filter'),
]