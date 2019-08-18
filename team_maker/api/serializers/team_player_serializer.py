from rest_framework import serializers
from team_maker.core.models import TeamPlayer
from team_maker.api.serializers import PlayerSerializer


class TeamPlayerSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = TeamPlayer
        fields = ('id', 'admin', 'points', 'player')
