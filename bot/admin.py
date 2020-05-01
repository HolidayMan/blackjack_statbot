from django.contrib import admin
from .models import *


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = ("tg_id", "first_name", "username", "date_joined")
    search_fields = ('username', "first_name")


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("name", "tg_id", "user_added")
    search_fields = ('name', "user_added")


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("game_id", "date", "no", "number", "status", "score", "p1_cards", "p2_cards")
    search_fields = ("game_id", "date", "no", "number", "status", "score", "p1_cards", "p2_cards")


@admin.register(GameMessage)
class GameMessageAdmin(admin.ModelAdmin):
    list_display = ("message_id", "game")
    search_fields = ('name', "user_added")
