from django.urls import path
from . import views

urlpatterns = [
    path('cities/', views.citiesView),
    path('cities/<int:pk>/', views.citiesView),
    path('cities/add/', views.citiesView),
    path('cities/delete/<int:pk>/', views.citiesView),
    path('cities/update/<int:pk>/', views.citiesView),
    path('divisions/', views.divisionsView),
    path('divisions/<int:pk>/', views.divisionsView),
    path('divisions/add/', views.divisionsView),
    path('divisions/delete/<int:pk>/', views.divisionsView),
    path('divisions/update/<int:pk>/', views.divisionsView),
    path('teams/', views.teamsView),
    path('teams/<int:pk>/', views.teamsView),
    path('teams/add/', views.teamsView),
    path('teams/delete/<int:pk>/', views.teamsView),
    path('teams/update/<int:pk>/', views.teamsView),
    path('players/', views.playersView),
    path('players/<int:pk>/', views.playersView),
    path('players/add/', views.playersView),
    path('players/delete/<int:pk>/', views.playersView),
    path('players/update/<int:pk>/', views.playersView),
    path('matches/', views.matchesView),
    path('matches/add/', views.matchesView),
    path('positions/', views.positionsView),
]
