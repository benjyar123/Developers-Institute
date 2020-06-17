from django.urls import path
from . import views


urlpatterns = [
    path("clubs", views.clubs, name="clubs"),
    path("clubs/<club_id>/details", views.club_details, name="club_details"),
    path("clubs/<club_id>/fixtures", views.club_fixtures, name="club_fixtures"),
    path("clubs/<club_id>/fixtures/add_fixture", views.add_fixture, name="add_fixture"),
    path("clubs/<club_id>/fixtures/player_availability", views.player_availability, name="player_availability"),
    path("clubs/<club_id>/squad", views.club_squad, name="club_squad"),
    path("clubs/<club_id>/fixtures/<fixture_id>/cancel_fixture", views.cancel_fixture, name="cancel_fixture"),
    path("clubs/<club_id>/fixtures/<fixture_id>/edit_fixture", views.edit_fixture, name="edit_fixture"),
    path("clubs/<club_id>/fixtures/<fixture_id>/select_team", views.select_team, name="select_team"),
    path("clubs/<club_id>/fixtures/<fixture_id>/tactics", views.tactics, name="tactics"),
    path("clubs/<club_id>/fixtures/<fixture_id>/post_match_stats", views.post_match_stats, name="post_match_stats"),
    path("clubs/<club_id>/results", views.results, name="results"),
    path("clubs/<club_id>/player_registration", views.player_registration, name="player_registration"),
    path("clubs/<club_id>/join_club", views.join_club, name="join_club"),
    path("clubs/<club_id>/edit_club_details", views.edit_club_details, name="edit_club_details"),
]


