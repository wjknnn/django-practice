from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomUserCreateSerializer, CustomUserSerializer, CustomTokenObtainPairSerializer, \
    UserNameSerializer

User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    serializer_class = CustomUserCreateSerializer


class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserNameSerializer
    permission_classes = [permissions.AllowAny]


class AdminListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
