from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import bookingSerializer, MenuItemSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import viewsets
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class bookingview(APIView):
    def get(self, request):
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
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    