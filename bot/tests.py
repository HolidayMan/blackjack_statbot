from django.test import TestCase
from bot.business_logic.parsing import Sender
from bot.parser import Games


json_data = {'draw': 0, 'recordsTotal': 374655, 'recordsFiltered': 374655, 'data': [['234732913', '02/05/2020', '21:50', '116', '3220', 'Live', '0:0', '', ''], ['234732652', '02/05/2020', '21:48', '115', '6745', 'Live', '0:0', '', ''], ['234732430', '02/05/2020', '21:46', '114', '4381', 'Live', '19:12', '7♠ J♠ 10♠', 'K♦ J♦ 6♦'], ['234732143', '02/05/2020', '21:44', '113', '1059', 'Dealer', '22:18', 'K♣ 9♦ 9♣', '8♥ 10♥'], ['234731839', '02/05/2020', '21:42', '112', '4950', 'Dealer', '23:17', '9♣ 6♠ J♦ 6♦', '8♠ 9♥'], ['234731742', '02/05/2020', '21:40', '111', '3335', 'Player', '18:17', '10♦ 8♣', '7♦ 8♦ J♣'], ['234731537', '02/05/2020', '21:38', '110', '4078', 'Player', '21:18', 'A♣ A♥', '7♥ A♠'], ['234731357', '02/05/2020', '21:36', '109', '2367', 'Player', '18:16', '6♠ J♠ 10♠', 'K♠ K♣ J♦ Q♦ Q♥'], ['234731204', '02/05/2020', '21:34', '108', '1536', 'Dealer', '27:17', '8♥ 8♣ A♠', 'A♥ 6♠'], ['234730985', '02/05/2020', '21:32', '107', '4402', 'Player', '21:10', 'A♣ 10♥', '7♥ Q♥']]}


class TestSenderString(TestCase):
    def setUp(self):
        self.games = Games.de_json(json_data).games

    def test_string(self):
        for game in self.games:
            print(Sender.get_message_text(game))
