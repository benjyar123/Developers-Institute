from django.urls import path
from . import views

urlpatterns = [
    path("compose_message", views.compose_message, name="compose_message"),
    path("compose_message/<club_id>", views.compose_club_message, name="compose_club_message"),
    path("message_user/<profile_id>", views.message_user, name="message_user"),
    path("read_message/<message_id>", views.read_message, name="read_message"),
    path("delete_message/<message_id>", views.delete_message, name="delete_message"),
    ]

