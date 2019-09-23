from team_maker.core import models
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.decorators import action
from rest_framework import generics, status
from rest_framework import viewsets
from team_maker.api import serializers
from team_maker.core import services


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

    def get_object(self):
        game = self.get_queryset().get(pk=self.kwargs['pk'])
        return game

    def create(self, request, *args, **kwargs):
        game = self.queryset.create(
            team_id=self.kwargs['team_pk'],
            date=request.data['date']
        )
        game.home_team = models.TeamGroup.objects.create(
            team_id=self.kwargs['team_pk'],
            game_id=game.id
        )
        game.away_team = models.TeamGroup.objects.create(
            team_id=self.kwargs['team_pk'],
            game_id=game.id
        )
        game.save()
        serializer = self.get_serializer()
        return Response(
            serializer.to_representation(game),
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['put'])
    def finish(self, request, *args, **kwargs):
        game = self.get_object()
        services.games.distribute_game_points(game)
        game.finished = True
        game.save()
        serializer = self.get_serializer()
        return Response(
            serializer.to_representation(game),
            status=status.HTTP_200_OK
        )


class AvailablePlayersView(viewsets.ViewSet,
                           generics.ListCreateAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.GameAvailablePlayer.objects
    serializer_class = serializers.GameAvailablePlayerSerializer

    def get_queryset(self):
        game = models.Game.objects.get(pk=self.kwargs['game_pk'])
        return game.available_players

