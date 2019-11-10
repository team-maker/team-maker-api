from team_maker.core import models
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics
from rest_framework import viewsets
from team_maker.api import serializers


class TeamGroupPlayerView(viewsets.ViewSet,
                          generics.ListAPIView,
                          generics.RetrieveAPIView,
                          generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.TeamGroupPlayer.objects
    serializer_class = serializers.TeamGroupPlayerSerializer

    def get_queryset(self):
        game = models.Game.objects.get(pk=self.kwargs['game_pk'])
        team_group_ids = [game.home_team.id, game.away_team.id]
        queryset = self.queryset.filter(
            team_group_id__in=team_group_ids
        ).order_by('-points_amount', 'team_player__position')
        return queryset
