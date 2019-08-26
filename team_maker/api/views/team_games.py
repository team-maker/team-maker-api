from team_maker.core import models
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics, status
from rest_framework import viewsets
from team_maker.api import serializers


class TeamGamesView(viewsets.ViewSet,
                    generics.ListCreateAPIView,
                    generics.RetrieveAPIView,
                    generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.Game.objects  # only users that can access the app
    serializer_class = serializers.TeamGameSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(team_id=self.kwargs['team_pk'])
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TeamGameSerializer
        if self.action == 'retrieve':
            return serializers.TeamGameDetailedSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        team = serializer.create(data, *args, **kwargs)
        player = self.request.user.player
        models.TeamPlayer.objects.create(team=team, player=player, admin=True)

        return Response(
            serializer.to_representation(team),
            status=status.HTTP_201_CREATED
        )

