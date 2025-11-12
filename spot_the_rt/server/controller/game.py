from player import Player
from dobbledeck import Dobbledeck


class Game():

    def __init__(self, nb_round:int = 47, connected_player:list = [], nb_connected_player:int = 0, lobby_name:str = "Partie", game_id:int = 1):
        self.__nb_round = nb_round
        self.__connected_player = connected_player
        self.__nb_connected_player = nb_connected_player
        self.__lobby_name = lobby_name
        self.__game_deck = Dobbledeck()
        self.__game_id = game_id

    def _set_nb_round(self, new_nb_round:int):
        self.__nb_round = new_nb_round

    def _add_connected_player(self, new_connected_player:object):
        self.__connected_player.append(new_connected_player)

    def _del_connected_player(self, connected_player_input:object):
        self.__connected_player.remove(connected_player_input)

    def _set_nb_connected_player(self, new_nb_connected_player:int):
        self.__nb_connected_player = new_nb_connected_player
    
    def _get_nb_round(self):
        return self.__nb_round

    def _get_connected_player(self):
        return self.__connected_player

    def _get_nb_connected_player(self):
        return self.__nb_connected_player

    def _get_lobby_name(self):
        return self.__lobby_name

    def _get_game_deck(self):
        return self.__game_deck

    def add_player_to_lobby(self, new_player_name:str, new_player_status:bool):
        new_player_card_id = self._get_nb_connected_player() + 1
        new_player = Player(new_player_name, new_player_status, new_player_card_id)
        self._set_nb_connected_player(new_player_card_id)
        self._add_connected_player(new_player)

    def remove_player_to_lobby(self, player_name_input:object):
        self._del_connected_player(connected_player_input=player_name_input)
