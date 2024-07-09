from rest_framework import viewsets

from apps.pages.api.serializers import TeamSerializer, TeamCreateSerializer
from apps.pages.models import Team
from utils.permissions import IsAdmin


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
