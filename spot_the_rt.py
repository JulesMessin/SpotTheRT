from dobbledeck import Dobbledeck
from game import Game
from player import Player

class SpotTheRT:

    def __init__(self, list_game:list = ["empty"], nb_game:int = 0):
        self.__list_game = list_game
        self.__nb_game = nb_game


    def _add_game(self, new_game_input):
        self.__list_game.append(new_game_input)

    def _get_list_game(self):
        return self.__list_game

    def _set_nb_game(self, new_nb_game):
        self.__nb_game = new_nb_game

    def _get_nb_game(self):
        return self.__nb_game

    def _is_in_list_game(self, lobby_name_input):
        if lobby_name_input in self._get_list_game:
            return True
        else:
            return False

    def inscription_request():
        pass

    def connexion_request():
        pass

    def create_lobby_request(lobby_name_input, player_pseudo_input):
        if _is_in_list_game(lobby_name_input):
            new_game_id = self._get_nb_game() + 1
            new_game = Game(lobby_name=lobby_name_input, game_id=new_game_id)
            self._set_nb_game(new_game_id)
            self._add_game(new_game)
            new_game.add_player_to_lobby(new_player_name=player_pseudo_input, new_player_status=True)
            return "3"
        else:
            return "11"

    def join_lobby_request(lobby_name_input, player_pseudo_input):
        try:
            game_id = self._get_list_game().index(lobby_name_input)

        except ValueError:
            return "12"


    def launch_game_request():
        pass

    def quit_game_request():
        pass

    def is_symbol_correct_request():
        pass

def main():
    pass

if __name__=='__main__':
    main()