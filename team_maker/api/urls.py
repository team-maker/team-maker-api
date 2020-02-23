from django.conf.urls import include, url
from team_maker.api import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import renderers
from rest_framework_nested import routers

router = routers.DefaultRouter(
    trailing_slash=False,
    root_renderers=(renderers.JSONRenderer, renderers.BrowsableAPIRenderer, )
)

router.register(r'users', views.UserView)
router.register(r'players', views.PlayersView)
players_router = routers.NestedSimpleRouter(router, r'players', lookup='player')
players_router.register(r'teams', views.PlayerTeamsView, basename='player-teams')
router.register(r'team-players', views.TeamPlayerView)
router.register(r'teams', views.TeamView)

teams_router = routers.NestedSimpleRouter(router, r'teams', lookup='team')
teams_router.register(r'current-team-player', views.CurrentTeamPlayerView, basename='team-player')
teams_router.register(r'games', views.TeamGamesView, basename='team-games')
teams_router.register(r'rules', views.TeamRulesView, basename='team-rules')

games_router = routers.NestedSimpleRouter(teams_router, r'games', lookup='game')
games_router.register(r'available-players', views.AvailablePlayersView, basename='available-players')
games_router.register(r'group-players', views.TeamGroupPlayerView, basename='team-group-players')
games_router.register(r'goals', views.GameGoalsView, basename='goals')
router.register(r'teams/token', views.TeamByTokenView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(players_router.urls)),
    url(r'^', include(teams_router.urls)),
    url(r'^', include(games_router.urls)),
    url(
        r'^teams/(?P<team_pk>[^/.]+)/team-players/(?P<team_player_pk>[^/.]+)/stats$',
        views.TeamPlayerStatsView.as_view(),
        name='team_player_stats'
    ),
    url(
        r'^teams/(?P<team_pk>[^/.]+)/team-players/(?P<team_player_pk>[^/.]+)/evaluate$',
        views.TeamPlayerEvaluationView.as_view(),
        name='team_player_evaluate'
    ),
    url(
        r'^teams/(?P<team_pk>[^/.]+)/games/(?P<game_pk>[^/.]+)/group-players/(?P<pk>[^/.]+)/points$',
        views.GroupPlayerPointsView.as_view(),
        name='group_player_points'
    ),
    url(r'^login$', obtain_jwt_token),
    url(r'^facebook-login$', views.FacebookLoginView.as_view(), name='facebook-login'),
]
