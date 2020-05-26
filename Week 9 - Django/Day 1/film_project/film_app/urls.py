from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("homepage", views.homepage, name="homepage"),
    path("addFilm", views.addFilm, name="addFilm"),
    path("addDirector", views.addDirector, name="addDirector"),
    path("editDirector/<id>", views.editDirector, name="editDirector"),
    path("editFilm/<id>", views.editFilm, name="editFilm"),
    path("editFilm/<id>", views.editFilm, name="editFilm"),
]
