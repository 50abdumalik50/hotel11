from django.urls import path

from apps.restaurants.views import RestaurantMenuListView, RestaurantMenuDetailView, indexView

urlpatterns =[
    path('', indexView.as_view(), name='index'),
    # path('list/', RestaurantListView.as_view(), name="restaurant_l"),
    # path('hours/list/', HoursListView.as_view(), name="hours_list"),
    path('restaurant_menu/list/', RestaurantMenuListView.as_view(), name="restaurant"),
    path('restaurant_menu/<int:pk>/', RestaurantMenuDetailView.as_view(), name="restaurant_detail"),

]