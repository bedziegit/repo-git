from django.urls import path
from . import views

urlpatterns = [
    path("welcome", views.welcome_view),
    path("persons", views.person_list),
]