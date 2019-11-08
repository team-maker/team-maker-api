from team_maker.core import models
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics
from rest_framework import viewsets
from team_maker.api import serializers


class GroupPlayerPointsView(viewsets.ViewSet,
                            generics.ListAPIView,
                            generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.Point.objects
    serializer_class = serializers.PointSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(
            team_group_player__pk=self.kwargs['group_player_pk']
        ).order_by('-points_amount')
        return queryset