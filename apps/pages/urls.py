from django.urls import path

from apps.pages.views import ServiceListView, TeamListView, FacilitiesListView, ContactListView, AboutListView, create_booking

urlpatterns = [
    path('service/list', ServiceListView.as_view(), name="service"),
    path('team/', TeamListView.as_view(), name="team"),
    path('facilities/', FacilitiesListView.as_view(), name="facilities"),
    path('contact/', ContactListView.as_view(), name="contact"),
    path('about/', AboutListView.as_view(), name="about"),
    path('create_booking/', create_booking, name='create_booking'),

]