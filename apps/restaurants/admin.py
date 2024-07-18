from django.contrib import admin

from apps.restaurants.models import Restaurant, Hour, Restaurant_Menu


@admin.register(Restaurant_Menu)
class RestaurantMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_type', 'price')
    list_filter = ('menu_type',)
    search_fields = ('name', 'description')