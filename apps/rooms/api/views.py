from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.rooms.api.serializers import RoomSerializer, RoomCreateSerializer, BookingSerializer, BookingCreateSerializer
from apps.rooms.models import Room, Booking
from utils.permissions import IsAdmin


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [IsAdmin]


def get_serializer_class(self):
    if self.action in ['create']:
        return RoomCreateSerializer
    elif self.action == 'retrieve':
        return RoomSerializer
    return self.serializer_class


class RoomUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# List and Create Room Views
# class RoomListCreateView(generics.ListCreateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


# Retrieve, Update and Delete Room Views
# class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [IsAdmin]


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def get_serializers_class(self):
    if self.action in ['create']:
        return BookingCreateSerializer
    elif self.action == 'retrieve':
        return BookingSerializer
    return self.serializer_class


class BookingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# class BookingsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


# class BookingRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
#
# class BookingUpdateView(generics.UpdateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#
#
# class BookingDestroyView(generics.DestroyAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
