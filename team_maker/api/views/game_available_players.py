from team_maker.core import models
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics
from rest_framework import viewsets
from team_maker.api import serializers


class AvailablePlayersView(viewsets.ViewSet,
                           generics.UpdateAPIView,
                           generics.ListAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.GameAvailablePlayer.objects
    serializer_class = serializers.GameAvailablePlayerSerializer

    def get_queryset(self):
        game = models.Game.objects.get(pk=self.kwargs['game_pk'])
        return game.available_players

