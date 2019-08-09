from team_maker.core import models
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics, status
from rest_framework import viewsets
from team_maker.api.serializers import TeamPlayerSerializer


class TeamPlayerView(viewsets.ViewSet,
                     generics.ListCreateAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.TeamPlayer.objects  # only users that can access the app
    serializer_class = TeamPlayerSerializer

    def create(self, request, *args, **kwargs):
        player = self.request.user.player
        data = request.data
        team_token = data['team_token']
        try:
            team = models.Team.objects.get(token=team_token)
        except models.Team.DoesNotExist:
            raise ValidationError('Team not found')

        instance = self.queryset.create(team=team, player=player, admin=True)
        serializer = self.get_serializer()
        return Response(
            serializer.to_representation(instance),
            status=status.HTTP_201_CREATED
        )
