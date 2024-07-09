from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.pages.api import views

router = DefaultRouter()
router.register('', views.TeamViewSet, basename="team_api")

urlpatterns = [

]
urlpatterns += router.urls