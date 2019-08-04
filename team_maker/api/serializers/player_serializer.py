from rest_framework import serializers
from team_maker.core.models import Player
from team_maker.api.serializers import UserSerializer


class UserPlayerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ('rating', 'user')


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('rating',)
