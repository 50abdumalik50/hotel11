from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.restaurants.api import views

router = DefaultRouter()


urlpatterns = [
    path('restaurant_crud/<int:pk>/', views.RestaurantRetrieveUpdateDestroyAPIView.as_view(), name='restaurant_crud'),
    path('restaurant_create/<int:pk>/', views.RestaurantListCreateView.as_view(), name='restaurant_create'),
    path('hour_create/<int:pk>/', views.HourListCreateView.as_view(), name='hour_create'),
    path('hour_crud/<int:pk>/', views.HourRetrieveUpdateDestroyAPIView.as_view(), name='hour_crud'),
    path('menu_create/<int:pk>/', views.RestaurantMenuListCreateView.as_view(), name='menu_create'),
    path('menu_crud/<int:pk>/', views.RestaurantMenuRetrieveUpdateDestroyAPIView.as_view(), name='menu_crud'),
]

urlpatterns += router.urls
