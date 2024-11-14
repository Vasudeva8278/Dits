from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserAccount
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [ 'username', 'email', 'contact_number']


class UserAccountSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Expecting a user ID (pk)

    class Meta:
        model = UserAccount
        fields = ['user', 'contact_number']

    def create(self, validated_data):
        user = validated_data.pop('user')  # Get the user instance using the pk
        contact_number = validated_data.pop('contact_number')  # Pop other data
        user_account = UserAccount.objects.create(user=user, contact_number=contact_number)
        return user_account


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()



class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
    
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
