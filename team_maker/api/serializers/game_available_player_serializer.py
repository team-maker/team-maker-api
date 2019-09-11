from rest_framework.serializers import ModelSerializer
from team_maker.api.serializers import TeamPlayerSerializer
from team_maker.core.models import GameAvailablePlayer


class GameAvailablePlayerSerializer(ModelSerializer):
    team_player = TeamPlayerSerializer(read_only=True)

    class Meta:
        model = GameAvailablePlayer
        fields = (
            'id',
            'team_player',
            'availability',
        )
