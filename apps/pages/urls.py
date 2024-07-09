from django.urls import path

from apps.pages.views import ServiceListView, TeamListView, FacilitiesListView, ContactListView, AboutListView, create_booking, TeamCreateView, TeamUpdateView, TeamDetailView, TeamDeleteView

urlpatterns = [
    path('service/list', ServiceListView.as_view(), name="service"),
    path('facilities/', FacilitiesListView.as_view(), name="facilities"),
    path('contact/', ContactListView.as_view(), name="contact"),
    path('about/', AboutListView.as_view(), name="about"),
    path('create_booking/', create_booking, name='create_booking'),


    path('team/', TeamListView.as_view(), name="team"),
    path('team/create/', TeamCreateView.as_view(), name='team-create'),
    # path('team/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('team/<int:pk>/update/', TeamUpdateView.as_view(), name='team-update'),
    path('team/<int:pk>/delete/', TeamDeleteView.as_view(), name='team-delete'),

]