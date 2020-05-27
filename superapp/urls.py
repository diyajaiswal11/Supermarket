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
    path('addcustomer/',views.addcustomer,name='addcustomer'),
    path('frontpage/',views.frontpage,name='frontpage'),
    path('addorder/<int:pk>',views.addorder,name='addorder'),
    path('viewcustomer/',views.viewcustomer,name='viewcustomer'),
    #path('deleteorder/<int:a>/<int:b>/',views.deleteorder,name='deleteorder'),
    
]
