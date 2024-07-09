from rest_framework import serializers

from apps.pages.models import Team


class TeamSerializer(serializers.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name',
            'occupation',
            'image_for_team',

        ]


class TeamCreateSerializer(serializers.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name',
            'occupation',
            'image_for_team',

        ]