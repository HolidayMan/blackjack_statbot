from django.test import TestCase
from bot.business_logic.parsing import Sender
from bot.parser import Parser


class TestSenderString(TestCase):
    def setUp(self):
        self.games = Parser('ebantiay', 'password').get_games().games

    def test_string(self):
        for game in self.games:
            print(Sender.get_message_text(game))
