from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from .models import *
from .serializers import *
from django.contrib.auth.models import Group

# Create your views here.

class BookGenreApiView(ModelViewSet):
    queryset = Book_genre.objects.all()
    serializer_class = BooksGenreSerializer
    
class AuthorApiView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class BooksApiView(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    
class OrderApiView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
@api_view(['POST'])
@permission_classes([AllowAny,]) #This permission class should always below the api view
def Login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=email, password=password)
    if user == None:
        return Response("Invalid Credentials",status=status.HTTP_404_NOT_FOUND)
    else:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(token.key)
    
@api_view(['POST'])
@permission_classes([AllowAny,]) #This permission class should always below the api view
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hash_password = make_password(password)
        a = serializer.save()
        a.password = hash_password
        a.save()
        return Response('User Created!', status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([AllowAny,]) #This permission class should always below the api view
def group(request):
    group_obj =Group.objects.all()
    serializer = GroupSerializer(group_obj,many=True)
    return Response(serializer.data)
