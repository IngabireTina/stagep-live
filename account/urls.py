from django.urls import path
from . import views
from .views import *


urlpatterns = [

    path('', views.homePage, name='homePage'),
    path('home', Dashboard.as_view(), name='home'),
    path('profile/', views.userProfile, name='profile'),

    # path('dashboard1/', views.profile, name='dashboard1'),
    # path('dashboard2/', views.finance, name='dashboard2'),

    path('register/', views.registerPage, name='register'),
    path('users/', views.allUser, name='users'),
    path('updateuser/<str:pk>/', views.updateUser, name='update_user'),
    path('deleteuser/<str:pk>/', views.deleteUser, name='delete_user'),

    path('address/', views.address, name='address'),

    path('update_address/<str:pk>/', views.updateAddress, name='update_address'),
    path('delete_address/<str:pk>/', views.deleteAddress, name='delete_address'),

    path('dashboard1/', Dashboard1.as_view(), name='dashboard1'),
    path('dashboard2/', views.dashboard2, name='dashboard2'),


]
