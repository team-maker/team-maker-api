from django.conf.urls import include, url
from team_maker.api import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import renderers, routers

router = routers.DefaultRouter(
    trailing_slash=False,
    root_renderers=(renderers.JSONRenderer, renderers.BrowsableAPIRenderer, )
)

router.register(r'users', views.UserView)
router.register(r'players', views.PlayersView)
router.register(r'team-players', views.TeamPlayerView)
router.register(r'teams', views.TeamView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login$', obtain_jwt_token),
    url(r'^facebook-login$', views.FacebookLoginView.as_view(), name='facebook-login'),
]
