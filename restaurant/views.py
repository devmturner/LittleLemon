from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import bookingSerializer, MenuItemSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class bookingview(APIView):
    def get(self, request):
        permission_classes = [IsAuthenticated]
        items = booking.objects.all()
        serializer = bookingSerializer(items, many= True)
        return Response(serializer.data) #Return JSON

class menuview(APIView):
    def get(self, request):
        items = menu.objects.all()
        serializer = menuSerializer(items, many= True)
        return Response(serializer.data)

    def post(self, request):
        serializer = menuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})

class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

@api_view()

@permission_classes([IsAuthenticated])

def msg(request):
    return Response({"message":"This view is protected"})