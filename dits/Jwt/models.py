from django.db import models
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView


class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)  # Ensure this field exists if required
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)


    def __str__(self):
        return self.name





