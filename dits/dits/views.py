from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import ValidationError
from .serializers import Userserializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('passowrd')
    
        if User.objects.filter(username=username).exists():
            raise ValidationError("user already exists")
    

        user = User.objects.create_user(username=username, password=password)
        user.save()
    
        return Response({"message":"user register sucessfully"},status=status.HTTP_201_CREATED)
    
class GetUserView(APIView):
   

    def get(self, request):
        # Retrieve all users
        users = User.objects.all()
        serializer = Userserializer(users,many=True)

        
        return Response({"message": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    




    

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Use .get() to safely access 'username' and 'password'
        username = request.data.get("username")
        password = request.data.get("password")

        # Ensure that username and password are both provided
        if not username or not password:
            raise AuthenticationFailed("Username and password are required")

        # Authenticate user
        user = authenticate(username=username, password=password)

        # Check if authentication failed
        if user is None:
            raise AuthenticationFailed("Invalid credentials")

        # Create JWT token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Print tokens to console (for testing purposes)
        print("Access Token:", access_token)
        print("Refresh Token:", str(refresh))

        # Return the response with the tokens
        return Response({
            "message": "Login successful",
            "access_token": access_token,
            "refresh_token": str(refresh)
        }, status=status.HTTP_200_OK)