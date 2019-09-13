from rest_framework.serializers import ModelSerializer, SerializerMethodField
from team_maker.core.models import Game
from team_maker.api.serializers import TeamGroupSerializer
from team_maker.api.serializers import TeamGroupPlayerSerializer


class TeamGameSerializer(ModelSerializer):
    home_team = TeamGroupSerializer(read_only=True)
    away_team = TeamGroupSerializer(read_only=True)
    num_goals = SerializerMethodField(read_only=True)
    generated_points = SerializerMethodField(read_only=True)
    mvps = SerializerMethodField(read_only=True)

    class Meta:
        model = Game
        fields = (
            'id',
            'date',
            'team_id',
            'finished',
            'num_goals',
            'mvps',
            'generated_points',
            'home_team',
            'away_team'
        )

    def get_num_goals(self, instance):
        return instance.goals.count()

    def get_generated_points(self, instance):
        if instance.finished:
            return instance.generated_points()
        return 0

    def get_mvps(self, instance):
        if instance.finished:
            mvps = instance.game_mvps()
            return TeamGroupPlayerSerializer(mvps, many=True).data
        return []
