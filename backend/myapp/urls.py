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
<<<<<<< HEAD
    path('profiles/', ProfileFilterView.as_view(), name='profile-filter'),
=======
    path('work_filter/', ProfileFilterView.as_view(), name='profile-filter'),
    
>>>>>>> 2b4044a03d2cd5e7ef1ac029d7922d533084a71f
]