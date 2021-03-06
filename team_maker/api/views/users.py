from team_maker.core import models
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import status, mixins, generics
from rest_framework import viewsets
from team_maker.api.serializers import UserSerializer, UserSerializerWithToken
from django.utils.crypto import get_random_string


class UserView(viewsets.ViewSet,
               mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.User.objects  # only users that can access the app
    serializer_class = UserSerializer

    def get_authenticators(self):
        if self.request.method == 'POST':
            return []
        return super(generics.GenericAPIView, self).get_authenticators()

    def get_permissions(self):
        if self.request.method == 'POST':
            return []
        return super(generics.GenericAPIView, self).get_permissions()

    def get_object(self):
        user = self.request.user
        return user

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserSerializerWithToken
        else:
            return UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class FacebookLoginView(mixins.UpdateModelMixin,
                        generics.GenericAPIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    queryset = models.User.objects  # only users that can access the app
    serializer_class = UserSerializerWithToken
    permission_classes = (AllowAny,)

    def get_object(self):
        queryset = self.get_queryset()
        try:
            obj = queryset.get(email=self.request.data['email'])
        except models.User.DoesNotExist:
            obj = queryset.create(email=self.request.data['email'])
            obj.set_password(get_random_string())
            obj.save()
        return obj

    def put(self, request, *args, **kwargs):
        request_data = request.data
        if 'name' in request_data.keys():
            names = request_data['name'].split(' ')
            request_data['first_name'] = names[0]
            request_data['last_name'] = names[-1]
            del(request_data['name'])
        else:
            request_data['first_name'] = 'CHANGE ME'
            request_data['last_name'] = 'CHANGE ME'

        serializer = self.get_serializer(data=request_data)
        updated_instance = serializer.update(self.get_object(), request_data)
        return Response(serializer.to_representation(updated_instance), status=status.HTTP_201_CREATED)
