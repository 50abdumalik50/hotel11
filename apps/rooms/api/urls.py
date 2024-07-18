from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.rooms.api import views

router = DefaultRouter()
router.register('rooms', views.RoomViewSet, basename="room_api")
router.register('bookings', views.BookingViewSet, basename="booking_api")

urlpatterns = [
    path('room/<int:pk>/', views.RoomUpdateDeleteRetrieveAPIView.as_view(), name='room_rest'),
    path('booking/<int:pk>/', views.BookingListCreateView.as_view(), name='create'),
    path('book/<int:pk>/', views.BookingRetrieveUpdateDestroyAPIView.as_view(), name='book'),
    # path('booking_detail/<int:pk>/', views.BookingRetrieveAPIView.as_view(), name='retrieve'),
    # path('booking_update/<int:pk>/', views.BookingUpdateView.as_view(), name='update'),
    # path('booking_destroy/<int:pk>/', views.BookingDestroyView.as_view(), name='destroy'),
]
urlpatterns += router.urls
