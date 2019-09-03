from rest_framework.serializers import ModelSerializer, SerializerMethodField
from team_maker.core.models import TeamGroupPlayer
from team_maker.api.serializers import TeamPlayerSerializer


class TeamGroupPlayerSerializer(ModelSerializer):
    team_player = TeamPlayerSerializer(read_only=True)
    points_amount = SerializerMethodField(read_only=True)

    class Meta:
        model = TeamGroupPlayer
        fields = ('id', 'team_player', 'points_amount')

    def get_points_amount(self, instance):
        return instance.get_points_amount()
