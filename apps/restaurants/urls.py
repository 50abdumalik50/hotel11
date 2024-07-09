from django.urls import path
from .views import RestaurantMenuListView, RestaurantMenuDetailView, RestaurantMenuCreateView, RestaurantMenuDeleteView, RestaurantMenuUpdateView

urlpatterns = [
    path('', RestaurantMenuListView.as_view(), name='index'),
    path('restaurant_menu/list/', RestaurantMenuListView.as_view(), name='restaurant'),
    path('restaurant_menu/create/', RestaurantMenuCreateView.as_view(), name='restaurant_create'),
    path('restaurant_menu/<int:pk>/update/', RestaurantMenuUpdateView.as_view(), name='restaurant_update'),
    path('restaurant_menu/<int:pk>/delete/', RestaurantMenuDeleteView.as_view(), name='restaurant_delete'),
]