from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model, authenticate
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token


# Create your views here.

User = get_user_model()

# -------------------------------
# Template Views (Frontend)
# ------------------------------
def register_template_view(request):
    """
    Render registration page and handle user registration via template.
    """
    message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username", "")

        if User.objects.filter(email=email).exists():
            message = "Email already exists"
        else:
            user = User.objects.create_user(email=email, password=password, username=username)
            message = "Registration successful"
            return redirect("login_template")

    return render(request, "accounts/register.html", {"message": message})


def login_template_view(request):
    """
    Render login page and handle user authentication via template.
    """
    message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            Token.objects.get_or_create(user=user)
            return redirect("profile_template")
        else:
            message = "Invalid credentials"

    return render(request, "accounts/login.html", {"message": message})


def profile_template_view(request):
    """
    Render user profile page. Redirect to login if user is not authenticated.
    """
    if not request.user.is_authenticated:
        return redirect("login_template")
    return render(request, "accounts/profile.html", {"user": request.user})


def logout_template_view(request):
    """
    Log out user and redirect to login page.
    """
    logout(request)
    return redirect("login_template")


#DRF endpoints
#user regitration
class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail" : "registration successfull"})

#user login view
class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "detail" : "Login successfull",
                'token': token.key,
                'email': user.email
            }, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
 
 #user profile view       
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
