from team_maker.core import models
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics, status
from rest_framework import viewsets
from team_maker.api import serializers


class TeamView(viewsets.ViewSet,
               generics.ListCreateAPIView,
               generics.RetrieveAPIView,
               generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.Team.objects  # only users that can access the app
    serializer_class = serializers.TeamSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

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


class TeamByTokenView(viewsets.ViewSet,
                      generics.RetrieveAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.Team.objects  # only users that can access the app
    serializer_class = serializers.TeamSerializer

    def get_object(self):
        token = self.kwargs['pk']
        return self.queryset.get(token=token)


class PlayerTeamsView(viewsets.ViewSet,
                      generics.ListAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.Team.objects  # only users that can access the app
    serializer_class = serializers.TeamSerializer

    def get_queryset(self):
        player_id = self.kwargs['player_pk']
        # import code; code.interact(local=dict(globals(), **locals()))
        teams = models.TeamPlayer.objects.filter(player_id=player_id).values_list('team_id', flat=True)
        queryset = self.queryset.filter(id__in=teams)
        return queryset
