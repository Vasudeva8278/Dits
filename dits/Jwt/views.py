from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserAccount
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import CustomPagination  # Import your custom pagination class
from .serializers import UserAccountSerializer,AccountSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, TokenSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import UserAccount
from .serializers import UserAccountSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import UserAccount
from .serializers import UserAccountSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignupSerializer
from .filters import UserAccountFilter
from .filters import UserAccountFilter
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class AddAccountView(APIView):
    def post(self, request, *args, **kwargs):
      
        serializer = UserAccountSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Account created successfully!',
                'account': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateAccountView(APIView):
    def put(self, request, id):
        try:
            account = UserAccount.objects.get(id=id)
        except UserAccount.DoesNotExist:
            return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserAccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Account updated successfully!', 'account': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeleteAccountView(APIView):
    def delete(self, request, id):
        try:
            account = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

        account.delete()
        return Response({'message': 'Account deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response({
                'message': 'User created successfully!',
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(TokenObtainPairView):
    serializer_class = TokenSerializer


class ProfileView(APIView):

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                user_account = UserAccount.objects.get(user=user)
                serializer = UserAccountSerializer(user_account)
                return Response({'profile': serializer.data}, status=status.HTTP_200_OK)
            except UserAccount.DoesNotExist:
                return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'User is not authenticated, please log in to access your profile'}, status=status.HTTP_200_OK)

        
class GetAllUsersView(APIView):
    permission_classes = [IsAuthenticated]  
    def get(self, request):
        users = User.objects.all()  
        serializer = UserSerializer(users, many=True)  
        return Response(serializer.data, status=200) 


class UserAccountListView(generics.ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = UserAccountFilter
    search_fields = ['username', 'email']
    ordering_fields = ['username', 'email']
    pagination_class = CustomPagination 
