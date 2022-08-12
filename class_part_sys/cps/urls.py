from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:module_id>', views.sessions, name="sessions"),
    path('<int:module_id>/generate', views.generate_session, name="generate")
]