import django_filters
from .models import UserAccount

class UserAccountFilter(django_filters.FilterSet):
    class Meta:
        model = UserAccount
        fields = ['username']  