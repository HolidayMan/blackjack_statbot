import requests
from bs4 import BeautifulSoup
from json.decoder import JSONDecodeError
import datetime


class Parser:
    session: requests.session = None
    username: str = None
    password: str = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_games(self, start=0, length=0):
        return Games.de_json(self.get_json(start, length))

    def get_json(self, start=0, length=10):
        url = f"https://cbets.su/stats/TwentyOne/Preloader?start={start}&length={length}"
        try:
            response = self.session.get(url)
            json_data = response.json()
            if not json_data['data']:
                raise AttributeError("data is empty")
        except (AttributeError, JSONDecodeError):
            self._get_session()
            return self.get_json()
        return json_data

    def _get_session(self):
        self.session = requests.session()
        self._register_session(self.username, self.password)
        return self.session

    def _register_session(self, username: str, password: str):
        data = {
            "credentials[username]": username,
            "credentials[password]": password,
            "redirect": "/cabinet",
            "_csrf": self._get_csrf_token(),
        }
        url = "https://cbets.su/user/authenticate"
        return self.session.post(url, data)

    def _get_csrf_token(self):
        response = self.session.get('https://cbets.su/user/login')
        soup = BeautifulSoup(response.text, "lxml")
        form = soup.find('form')
        csrf_token = form.find('input', {'name': "_csrf"})['value']
        return csrf_token


class Games:
    draw = None
    records_total = None
    records_filtered = None
    parser = None

    def __init__(self, draw, records_total, records_filtered, games):
        self.draw = draw
        self.records_total = records_total
        self.recordsFiltered = records_filtered
        self.games = games

    @classmethod
    def de_json(cls, json_data):
        data = json_data['data']
        games = [Game(*game) for game in data]
        draw = json_data['draw']
        records_total = json_data['recordsTotal']
        records_filtered = json_data['recordsFiltered']
        return Games(draw, records_total, records_filtered, games)


class Game:
    game_id = None
    date = None
    time = None
    no = None
    number = None
    status = None
    score = None
    p1_cards = None
    p2_cards = None

    def __init__(self, game_id, date, time, no, number, status, score, p1_cards, p2_cards):
        self.game_id = game_id
        self.datetime = datetime.datetime.strptime(f"{date} {time}", '%d/%m/%Y %H:%M')
        self.date = self.datetime.date()
        self.time = self.datetime.time()
        self.no = no
        self.number = number
        self.status = status
        self.score = score
        self.p1_cards = p1_cards
        self.p2_cards = p2_cards

    def __repr__(self):
        return f"<Game {self.game_id}>"
