from rest_framework.serializers import ModelSerializer, SerializerMethodField
from team_maker.core.models import PlayerEvaluation
from team_maker.api.serializers import TeamPlayerSerializer


class EvaluationSerializer(ModelSerializer):
    evaluated_player = TeamPlayerSerializer(read_only=True)
    evaluator_player = TeamPlayerSerializer(read_only=True)

    class Meta:
        model = PlayerEvaluation
        fields = (
            'id',
            'evaluated_player',
            'evaluator_player',
            'rating'
        )
