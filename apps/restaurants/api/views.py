from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.restaurants.api.serializers import RestaurantSerializer, RestaurantCreateSerializer, HourSerializer, HourCreateSerializer, RestaurantMenuSerializer, RestaurantMenuCreateSerializer

from apps.restaurants.models import Restaurant, Restaurant_Menu, Hour


class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return RestaurantCreateSerializer
    elif self.action == 'retrieve':
        return RestaurantSerializer
    return self.serializer_class


class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class HourListCreateView(generics.ListCreateAPIView):
    queryset = Hour.objects.all()
    serializer_class = HourSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return HourCreateSerializer
    elif self.action == 'retrieve':
        return HourSerializer
    return self.serializer_class


class HourRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hour.objects.all()
    serializer_class = HourSerializer


class RestaurantMenuListCreateView(generics.ListCreateAPIView):
    queryset = Restaurant_Menu.objects.all()
    serializer_class = RestaurantMenuSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return RestaurantMenuCreateSerializer
    elif self.action == 'retrieve':
        return RestaurantMenuSerializer
    return self.serializer_class


class RestaurantMenuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant_Menu.objects.all()
    serializer_class = RestaurantMenuSerializer