from django.urls import path
from .views import SignupView,AddAccountView, UpdateAccountView, DeleteAccountView, LoginView, ProfileView, GetAllUsersView,UserAccountListView
urlpatterns = [
   
    path('accounts/', AddAccountView.as_view(), name='add_account'),  
    path('update/<int:id>/', UpdateAccountView.as_view(), name='update_account'),
    path('filter/', UserAccountListView.as_view(), name='list_accounts'),
    path('<int:id>/delete/', DeleteAccountView.as_view(), name='delete_account'),  
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),  
    path('profile/', ProfileView.as_view(), name='profile'), 
    path('getall/',GetAllUsersView.as_view(),name='getuser') 
]
