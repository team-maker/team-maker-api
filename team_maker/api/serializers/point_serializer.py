from rest_framework.serializers import ModelSerializer
from team_maker.core.models import Point


class PointSerializer(ModelSerializer):

    class Meta:
        model = Point
        fields = ('id', 'points_amount')

