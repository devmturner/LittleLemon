from django.urls import path
from . import views
from .views import bookingview, menuview
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', bookingview.as_view()),
]