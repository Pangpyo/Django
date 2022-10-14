from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("read/", views.read, name="read"),
    path("alarm/<int:routine_pk>", views.alarm, name="alarm"),
    path("delete/<int:routine_pk>", views.delete, name="delete"),
]
