from rest_framework import serializers

from apps.rooms.models import Room, Booking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'room_type',
            'number',
            'number_of_beds',
            'image_for_room',
            'price',
            'startDate',
            'endDate',
        ]


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'room_type',
            'number',
            'number_of_beds',
            'image_for_room',
            'price',
            'startDate',
            'endDate',
        ]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'user',
            'room',
            'check_in_date',
            'check_out_date',
            'date_of_reservation',
        ]


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'user',
            'room',
            'check_in_date',
            'check_out_date',
            'date_of_reservation',
        ]
