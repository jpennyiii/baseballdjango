from django.contrib import admin
from django.contrib.admin import display
from .models import Position, Person, Club, Play, Match

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
	list_display=("description",)
	search_fields=("description",)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	list_display=("firstname",)
	search_fields=("firstname",)	
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
	list_display=("name",)
	search_fields=("name",)
@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display=("team",)
    search_fields=("team",)
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display=("game_date",)
    search_fields=("game_date",)
# Register your models here.
