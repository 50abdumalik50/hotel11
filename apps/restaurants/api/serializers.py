from rest_framework import serializers

from apps.restaurants.models import Restaurant, Hour, Restaurant_Menu


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'title',
            'description',
        ]


class RestaurantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'title',
            'description',
        ]


class HourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hour
        fields = [
            'meal_type',
            'startDate',
            'endDate',

        ]


class HourCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hour
        fields = [
            'meal_type',
            'startDate',
            'endDate',

        ]


class RestaurantMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_Menu
        fields = [
            'menu_type',
            'name',
            'description',
            'price',
        ]


class RestaurantMenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_Menu
        fields = [
            'menu_type',
            'name',
            'description',
            'price',
        ]