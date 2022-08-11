from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('session/<int:module_id>', views.sessions, name="sessions"),
]