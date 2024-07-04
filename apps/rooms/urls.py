from django.urls import path

from apps.rooms.views import (
    RoomListView,
    RoomCreateView,
    RoomUpdateView,
    RoomDeleteView,
    RoomDetailView,
    BookingDeleteView,
    BookingCreateView,
    BookingDetailView,
    BookingUpdateView,
    indexView,
    create_booking
    )


urlpatterns = [
    path('', indexView.as_view(), name='index'),
    path('create_booking/', create_booking, name='create_booking'),
    path('room/', RoomListView.as_view(), name="rooms_list"),
    path('room/create/', RoomCreateView.as_view(), name="room_create"),
    path('room/<int:pk>/', RoomDetailView.as_view(), name="room_details_AS"),
    path('room/<int:pk>/delete/', RoomDeleteView.as_view(), name="room_delete"),
    path('room/<int:pk>/update/', RoomUpdateView.as_view(), name="room_update"),
    path('booking/create/', BookingCreateView.as_view(), name="booking_form"),
    path('booking/<int:pk>/', BookingDetailView.as_view(), name="booking_detail"),
    path('booking/<int:pk>/delete/', BookingDeleteView.as_view(), name="booking_delete"),
    path('booking/<int:pk>/update/', BookingUpdateView.as_view(), name="booking_update"),
]