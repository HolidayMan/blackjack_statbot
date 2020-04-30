import requests
from bs4 import BeautifulSoup
import lxml


def get_json(session, start=0, length=10):
    url = f"https://cbets.su/stats/TwentyOne/Preloader?start={start}&length={length}"
    response = session.get(url)
    return response.json()


def get_session(username, password):
    session = requests.session()
    register_session(session, username, password)
    return session


def register_session(session, username, password):
    response = session.get('https://cbets.su/user/login')
    soup = BeautifulSoup(response.text, "lxml")
    form = soup.find('form')
    csrf_token = form.find('input', {'name': "_csrf"})['value']
    data = {
        "credentials[username]": username,
        "credentials[password]": password,
        "redirect": "/cabinet",
        "_csrf": csrf_token,
     }
    url = "https://cbets.su/user/authenticate"
    response = session.post(url, data)
