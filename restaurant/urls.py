from django.urls import path
from . import views
from .views import bookingview, menuview
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', bookingview.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('message/', views.msg),
]