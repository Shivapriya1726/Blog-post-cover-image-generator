from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('signin/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logoutUser,name='logoutUser'),

]
