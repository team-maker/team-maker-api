from team_maker.core import models
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics, status, mixins
from rest_framework import viewsets
from rest_framework.views import APIView
from team_maker.api.serializers import TeamPlayerSerializer
from team_maker.api.serializers import TeamPlayerStatsSerializer


class TeamPlayerView(viewsets.ViewSet,
                     generics.ListCreateAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.TeamPlayer.objects.order_by('-points_total')
    serializer_class = TeamPlayerSerializer

    def create(self, request, *args, **kwargs):
        player = self.request.user.player
        data = request.data
        team_token = data['team_token']
        try:
            team = models.Team.objects.get(token=team_token)
        except models.Team.DoesNotExist:
            raise ValidationError('Team not found')

        instance, created = self.queryset.get_or_create(team=team, player=player)
        for game in team.games.filter(finished=False).all():
            models.GameAvailablePlayer.objects.get_or_create(
                game=game,
                team_player=instance
            )
        serializer = self.get_serializer()
        return Response(
            serializer.to_representation(instance),
            status=status.HTTP_201_CREATED
        )


class CurrentTeamPlayerView(viewsets.ViewSet,
                            generics.ListAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.TeamPlayer.objects
    serializer_class = TeamPlayerStatsSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(team_id=self.kwargs['team_pk'])
        return queryset

    def list(self, request, *args, **kwargs):
        player = self.request.user.player
        instance = self.queryset.get(
            team_id=self.kwargs['team_pk'],
            player=player
        )
        serializer = self.get_serializer()
        return Response(
            serializer.to_representation(instance),
        )


class TeamPlayerStatsView(mixins.RetrieveModelMixin,
                          generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.TeamPlayer.objects.order_by('-points_total')
    serializer_class = TeamPlayerStatsSerializer

    def get_object(self):
        obj = self.queryset.get(id=self.kwargs['team_player_pk'])
        return obj

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TeamPlayerEvaluationView(APIView):

    def put(self, request, pk):
        user = self.request.data['user']
        team = models.Team.get(pk=self.kwargs['team_pk'])
        evaluator_player = models.TeamPlayer.get(
            team__pk=team.pk,
            player__pk=user.player.pk,
        )
        player_evaluation, created = self.queryset.get_or_create(
            evaluator_player__pk=evaluator_player.pk,
            evaluated_player__pk=self.kwargs['team_player_pk'],
        )
        player_evaluation.rating = self.request.data['rating']
        player_evaluation.save()
        return Response(status=status.HTTP_204_NO_CONTENT)