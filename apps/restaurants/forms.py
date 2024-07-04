from apps.restaurants.models import Restaurant, Hour, Restaurant_Menu
from django import forms


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'title',
            'description',
        ]


class HoursForm(forms.ModelForm):
    class Meta:
        model = Hour
        fields = [
            'meal_type',
            'startDate',
            'endDate',
        ]


class RestaurantMenuForm(forms.ModelForm):
    class Meta:
        model = Restaurant_Menu
        fields = [
            'menu_type',
            'name',
            'description',
            'price',
        ]

