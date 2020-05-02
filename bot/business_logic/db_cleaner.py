import logging
from bot.models import Game
from threading import Thread
from time import sleep


class DBCleaner:
    thread: Thread = None

    def __init__(self, timeout=3600):
        self.set_thread(timeout)

    def infinity_clean(self, timeout=10):
        while True:
            sleep(timeout)
            self.clean()

    def set_thread(self, timeout=10):
        self.thread = Thread(target=self.infinity_clean, args=(timeout,), daemon=True)
        return self.thread

    def start_thread(self):
        self.thread.start()

    @staticmethod
    def clean():
        games = Game.objects.all()[::-1][10:]
        for obj in games:
            obj.delete()
