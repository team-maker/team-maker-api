from rest_framework import serializers
from team_maker.core.models import Player


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('rating',)
