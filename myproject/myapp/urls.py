from django.urls import path, include
from . import views

urlpatterns = [
    path("welcome", views.welcome_view),
    path("persons", views.person_list),
    path('api/', include('myapp.api_urls'),)
]