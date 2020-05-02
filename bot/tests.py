from django.test import TestCase
from bot.business_logic.parsing import Sender
from bot.parser import Parser

json_data = {'draw': 0, 'recordsTotal': 374582, 'recordsFiltered': 374582, 'data': [['234715892', '02/05/2020', '19:12', '37', '2353', 'Live', '0:0', '', ''], ['234715679', '02/05/2020', '19:10', '36', '7767', 'Live', '0:0', '', ''], ['234715448', '02/05/2020', '19:08', '35', '4465', 'Live', '19:14', '7♠ 9♠ Q♦', 'J♣ K♣ 8♦'], ['234715250', '02/05/2020', '19:06', '34', '2218', 'Player', '21:19', '6♥ J♣ K♥ 9♠', 'Q♦ 6♦ 7♥ Q♠'], ['234714919', '02/05/2020', '19:04', '33', '6486', 'Dealer', '23:13', 'K♥ J♠ 6♦ A♥', 'Q♦ 10♥'], ['234714414', '02/05/2020', '19:02', '32', '1557', 'Player', '20:19', '9♣ K♦ 7♠', 'A♣ 8♠'], ['234714220', '02/05/2020', '19:00', '31', '7358', 'Dealer', '24:18', '9♠ K♠ A♠', '7♣ A♣'], ['234714017', '02/05/2020', '18:58', '30', '5075', 'Dealer', '23:19', '8♥ K♦ A♥', '8♠ A♦'], ['234713862', '02/05/2020', '18:56', '29', '1921', 'Draw', '20:20', 'Q♣ 7♦ 10♣', 'Q♠ 8♦ J♥ Q♥ K♥'], ['234713710', '02/05/2020', '18:54', '28', '5410', 'Player', '19:17', '8♣ A♠', '9♣ 6♠ J♥']]}


class TestSenderString(TestCase):
    def setUp(self):
        self.games = Parser('ebantiay', 'password').get_games().games

    def test_string(self):
        for game in self.games:
            print(Sender.get_message_text(game))
