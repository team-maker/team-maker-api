from rest_framework.serializers import ModelSerializer, SerializerMethodField
from team_maker.core.models import Game
from team_maker.api.serializers import TeamGroupSerializer
from team_maker.api.serializers import TeamGroupPlayerSerializer


class TeamGameSerializer(ModelSerializer):
    num_goals = SerializerMethodField(read_only=True)
    generated_points = SerializerMethodField(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'date', 'finished' 'num_goals', 'generated_points')

    def get_num_goals(self, instance):
        return instance.goals.count()

    def get_generated_points(self, instance):
        return instance.generated_points()


class TeamGameDetailedSerializer(ModelSerializer):
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
        return instance.generated_points()

    def get_mvps(self, instance):
        mvps = instance.game_mvps()
        return TeamGroupPlayerSerializer(mvps, many=True).data
