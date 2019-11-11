from team_maker.core import models
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics, status
from team_maker.api.serializers import EvaluationSerializer


class TeamPlayerEvaluationView(generics.UpdateAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.PlayerEvaluation.objects
    serializer_class = EvaluationSerializer

    def put(self, request, *args, **kwargs):
        player_evaluation = self.get_object()
        player_evaluation.rating = self.request.data['rating']
        player_evaluation.save()
        return Response(status=status.HTTP_204_NO_CONTENT)