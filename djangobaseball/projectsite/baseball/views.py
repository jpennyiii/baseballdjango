from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from baseball.models import Position, Person, Club, Play, Match

class HomePageView(ListView):
	model = Play
	context_object_name = 'play'
	template_name = "landingpage/home.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
	paginate_by = 2
		
class ClubView(ListView):
	model = Club
	context_object_name = 'club'
	template_name = "club.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def get_queryset(self, *args, **kwargs):
		qs = super(ClubView, self).get_queryset(*args, **kwargs)
		return qs
	paginate_by = 2

class PlayerView(ListView):
	model = Person
	context_object_name = 'player'
	template_name = "player.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def get_queryset(self, *args, **kwargs):
		qs = super(PlayerView, self).get_queryset(*args, **kwargs)
		return qs
	paginate_by = 3

class MatchView(ListView):
   model = Match
   context_object_name = 'match'
   template_name = "match.html"
   paginate_by = 2
# class MatchView(ListView):
# 	model = Match
# 	context_object_name = 'match'
# 	template_name = "match.html"
	
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		return context

# 	def get_queryset(self, *args, **kwargs):
# 		qs = super(ClubView, self).get_queryset(*args, **kwargs)
# 		return qs
# Create your views here.
