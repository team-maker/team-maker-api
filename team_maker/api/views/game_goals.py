from team_maker.core import models
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from team_maker.api import serializers


class GameGoalsView(viewsets.ViewSet,
                    generics.ListCreateAPIView,
                    generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.Goal.objects  # only users that can access the app
    serializer_class = serializers.GoalSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(game_id=self.kwargs['game_pk'])
        return queryset

    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.create(
            scorer_id=request.data['scorer_id'],
            game_id=self.kwargs['game_pk']
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
