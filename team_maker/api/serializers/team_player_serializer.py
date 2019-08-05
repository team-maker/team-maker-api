from rest_framework import serializers
from team_maker.core.models import TeamPlayer
from team_maker.api.serializers import TeamSerializer


class TeamPlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = TeamPlayer
        fields = ('id', 'team', 'admin', 'points')
