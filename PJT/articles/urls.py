from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("read/<int:account_pk>", views.read, name="read"),
    path("alarm/<int:account_pk>/<int:routine_pk>", views.alarm, name="alarm"),
    path("delete/<int:account_pk>/<int:routine_pk>", views.delete, name="delete"),
    path("update/<int:routine_pk>", views.update, name="update"),
    path("days/<int:account_pk>", views.days, name="days"),
    path("detail/<int:account_pk>/<int:routine_pk>", views.detail, name="detail"),
    path("result/<int:account_pk>/<int:routine_pk>", views.result, name="result"),
]
