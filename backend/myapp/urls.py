from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    UserRegisterView,
    UserLoginView,
    UpdateRatingView,
    UserProfileUpdateView,
    ProfileFilterView
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('update-rating/', UpdateRatingView.as_view(), name='update_rating'),
    path('user-profile/<str:username>/', UserProfileUpdateView.as_view(), name='user-profile'),
    path('profiles/', ProfileFilterView.as_view(), name='profile-filter'),
]