from django.urls import path
from . import views
from .views import UserProfileView


urlpatterns = [
    path("register/", views.UserRegistration.as_view(), name="user-registration"),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]