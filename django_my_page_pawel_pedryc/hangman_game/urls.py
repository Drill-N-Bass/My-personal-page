from django.urls import path

from . import views

urlpatterns = [
	path('hangman_game/', views.easter_egg_hangman_game)
]