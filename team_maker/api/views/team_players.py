from team_maker.core import models
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics
from team_maker.api import serializers


class TeamPlayerView(generics.ListAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.TeamPlayer.objects  # only users that can access the app
    serializer_class = serializers.TeamPlayerSerializer

    def get_queryset(self):
        user = self.request.user
        player = user.player
        return player.team_players.all()
