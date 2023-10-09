from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.CustomAuthToken.as_view(), name='login'),
    path('traders/', views.TraderList.as_view(), name='traders_list'),
    path('trader/<int:pk>/', views.Trader.as_view(), name='trader'),
]