from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
#django.contrib.auth.views.LoginView

urlpatterns = [
    path('',views.home,name='home'),
    path('loginpage/',views.loginpage, name='loginpage'),
    path('logoutpage/',views.logoutpage, name='logoutpage'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('editproduct/<int:pk>',views.editproduct,name='editproduct'),
    path('deleteproduct/<int:pk>',views.deleteproduct,name='deleteproduct'),
    #path('register/',views.register,name='register'),
    path('frontpage/',views.frontpage,name='frontpage'),
    #url('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    #url('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
