from django.db import models


class TgUser(models.Model):
    tg_id = models.IntegerField()
    first_name = models.CharField(max_length=64, blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.username:
            return self.username
        else:
            return str(self.id)


class Chat(models.Model):
    tg_id = models.IntegerField()
    name = models.CharField(max_length=64, blank=True, null=True)
    user_added = models.ForeignKey('TgUser', on_delete=models.CASCADE, related_name="chat")

    def __str__(self):
        return self.name


class Game(models.Model):
    game_id = models.CharField(max_length=64, unique=True)
    date = models.DateTimeField()
    no = models.CharField(max_length=64)
    number = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    score = models.CharField(max_length=64)
    p1_cards = models.CharField(max_length=64, blank=True, null=True)
    p2_cards = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.game_id


class GameMessage(models.Model):
    message_id = models.IntegerField()
    chat = models.ForeignKey('Chat', related_name="game_messages", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", related_name="game_message", on_delete=models.CASCADE)

    def __str__(self):
        return self.game
