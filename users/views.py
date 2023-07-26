from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from users.models import UserModel
from users.serializers import UserSerializer


# Create your views here.
class UserCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    permission_classes = ()


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]