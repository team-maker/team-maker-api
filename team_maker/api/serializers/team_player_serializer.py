from rest_framework import serializers
from team_maker.core.models import Player
from team_maker.api.serializers import TeamSerializer


class TeamPlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ('team', 'admin', 'points')
