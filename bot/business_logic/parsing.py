from threading import Thread
from time import sleep

from bot.parser import Parser, Game
from bot import BOT
from bot.models import Chat, GameMessage
from bot.models import Game as GameModel
import re


class ThreadedParser:
    parser: Parser = None
    thread: Thread = None

    def __init__(self, login, password, timeout=10):
        self.parser = Parser(login, password)
        self.set_parsing_thread(timeout)
        self.sender = Sender()

    def long_parse(self, timeout=10):
        while True:
            for game in self.parser.get_games().games[::-1]:
                self.sender.send(game)
            sleep(timeout)

    def set_parsing_thread(self, timeout=10):
        self.thread = Thread(target=self.long_parse, args=(timeout,), daemon=True)
        return self.thread

    def start_thread(self):
        self.thread.start()


class Sender:

    def send(self, game):
        if GameModel.objects.filter(game_id=game.game_id).exists():
            if not GameModel.objects.get(game_id=game.game_id).status != "Live":
                self.edit_messages(game)
        else:
            self.send_messages(game)

    def edit_messages(self, game):
        game_model, changed = self._update_or_create_game(game)
        chats = Chat.objects.filter(send=True)
        for chat in chats:
            if changed:
                message_id = GameMessage.objects.get(chat=chat, game=game_model).message_id
                BOT.edit_message_text(text=self.get_message_text(game), chat_id=chat.tg_id, message_id=message_id)

    def send_messages(self, game):
        game_model = self._update_or_create_game(game)
        chats = Chat.objects.filter(send=True)
        for chat in chats:
            message = BOT.send_message(chat.tg_id, self.get_message_text(game))
            self._save_message(game_model, chat, message)

    @staticmethod
    def get_message_text(game: Game):
        p1_score, p2_score = map(int, game.score.split(':'))
        total = p1_score + p2_score
        p1_cards, p2_cards = game.p1_cards, game.p2_cards
        game_number = game.no

        if p1_score == 21 or p2_score == 21:
            get_21 = " #O"
        else:
            get_21 = " "

        golden_point_pattern = r"A.( )*A."
        if p1_score == 21 and re.match(golden_point_pattern, p1_cards):
            golden_point = " #G"
            p1_score = 22
        elif p2_score == 21 and re.match(golden_point_pattern, p2_cards):
            golden_point = " #G"
            p2_score = 22
        else:
            golden_point = " "

        if game.status == "Live":
            message = f"#N{game_number}. {p1_score}({p1_cards})⏰{p2_score}({p2_cards})#T{total}"
        elif game.status == "Dealer":
            message = f"#N{game_number}. {p1_score}({p1_cards})-✅{p2_score}({p2_cards})#T{total}{get_21}{golden_point}"
        elif game.status == "Player":
            message = f"#N{game_number}. ✅{p1_score}({p1_cards})-{p2_score}({p2_cards})#T{total}{get_21}{golden_point}"
        elif game.status == "Draw":
            message = f"#N{game_number}. {p1_score}({p1_cards})❎{p2_score}({p2_cards})#T{total} #X{get_21}{golden_point}"
        else:
            raise ValueError(f"incorrect status value '{game.status}'")
        return message

    @staticmethod
    def _update_or_create_game(game):
        game_id = game.game_id
        datetime = game.datetime
        no = game.no
        number = game.number
        status = game.status
        score = game.score
        p1_cards = game.p1_cards
        p2_cards = game.p2_cards

        if GameModel.objects.filter(game_id=game_id).exists():
            game = GameModel.objects.get(game_id=game_id)
            if game.score != score:
                game.status = status
                game.score = score
                game.p1_cards = p1_cards
                game.p2_cards = p2_cards
                game.save()
                return game, True
            return game, False
        else:
            return GameModel.objects.create(game_id=game_id,
                                            date=datetime,
                                            no=no,
                                            number=number,
                                            status=status,
                                            score=score,
                                            p1_cards=p1_cards,
                                            p2_cards=p2_cards)

    @staticmethod
    def _save_message(game_model, chat_model, message):
        game_message = GameMessage.objects.get_or_create(message_id=message.message_id, game=game_model,
                                                         chat=chat_model)
        return game_message
