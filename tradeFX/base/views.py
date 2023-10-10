from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Trader
from .serializers import TraderSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Trader.objects.create(user=user, name=user.username, balance=100.00)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context = {'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id, 'username': user.username})

class TraderList(generics.ListCreateAPIView):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

class Trader(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['profit_loss'] = instance.balance - 100
        return Response(data)
