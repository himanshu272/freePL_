from django.urls import path,include
from app import views
from app.views import leaderboardViewSet

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('matches/$', views.matches , name='matches'),
    path('match/(?P<id>[0-9]+)$', views.create_team , name='create_team'),
    path('rules/$', views.rules , name='rules'),
    path('leaderboard/$', views.leaderboard , name='leaderboard'),
    path('listteams', views.listTeams , name='list_team'),
    path('matchpoints', views.matchpoints , name='matchpoints'),
    path('api/scoreboard',leaderboardViewSet.as_view(), name='view-leaderboard'),
]
