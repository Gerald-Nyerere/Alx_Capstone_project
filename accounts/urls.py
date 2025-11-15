from django.urls import path
from . import views
from .views import UserProfileView
from .views import (register_template_view, login_template_view, profile_template_view, logout_template_view)


urlpatterns = [
    path("account/register/", register_template_view, name="register_template"),
    path("account/login/", login_template_view, name="login_template"),
    path("account/profile/", profile_template_view, name="profile_template"),
    path("account/logout/", logout_template_view, name="logout_template"),

    #DRF APIs endpoint
    path("api/register/", views.UserRegistration.as_view(), name="user-registration"),
    path('api/login/', views.UserLoginView.as_view(), name='user-login'),
    path('api/profile/', UserProfileView.as_view(), name='profile'),
]