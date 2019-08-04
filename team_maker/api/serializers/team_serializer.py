from rest_framework import serializers
from team_maker.core.models import Team
from team_maker.api.serializers import UserPlayerSerializer


class TeamSerializer(serializers.ModelSerializer):
    players = UserPlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('name', 'players')
