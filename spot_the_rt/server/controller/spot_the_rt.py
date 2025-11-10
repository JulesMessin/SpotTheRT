from dobbledeck import Dobbledeck
from game import Game
from player import Player

class SpotTheRT:

    def __init__(self, list_game:list = [], nb_game:int = 0):
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

    def create_lobby_request(self, lobby_name_input, player_pseudo_input):
        if not self._is_in_list_game(lobby_name_input):
            new_game_id = self._get_nb_game() + 1
            new_game = Game(lobby_name=lobby_name_input, game_id=new_game_id)
            self._set_nb_game(new_game_id)
            self._add_game(new_game)
            new_game.add_player_to_lobby(new_player_name=player_pseudo_input, new_player_status=True)
            """ ENVOYER '1' (requête créer un lobby reussit) AU DEMANDEUR """
        else:
            """ ENVOYER '6' (requête rejoindre un lobby echouée) AU DEMANDEUR """

    def join_lobby_request(self, lobby_name_input, player_pseudo_input):
        if self._is_in_list_game(lobby_name_input):
            game_id = self._get_list_game().index(lobby_name_input) + 1
            self._get_list_game()[game_id]._add_player_to_lobby(new_player_name=player_pseudo_input, new_player_status=False)
            """ ENVOYER '2' (requête rejoindre un lobby reussit) AU DEMANDEUR """
        else:
            """ ENVOYER '7' (requête rejoindre un lobby echouée) AU DEMANDEUR """

    def launch_game_request(self, lobby_name_input):
        if self._is_in_list_game(lobby_name_input):
            game_id = self._get_list_game().index(lobby_name_input)
            selected_game = self._get_list_game()[game_id]
            for player_id in range(1, selected_game._get_nb_connected_player):
                requested_common_card = selected_game._get_game_deck()._get_card(0)
                requested_player_card = selected_game._get_game_deck()._get_card(player_id)
                """ ENVOYER '3'  (lancer une partie reussi) et LES CARTES AU JOUEUR SELON 'player_id' """
        else:
            """ ENVOYER '8' (requête lancer une partie echouée) AU DEMANDEUR """

    def quit_game_request(self, player_pseudo_input, lobby_name_input):
        if self._is_in_list_game(lobby_name_input):
            game_id = self._get_list_game().index(lobby_name_input)
            selected_game = self._get_list_game()[game_id]
            player_id = -1
            correct = False
            while not correct and player_id <= selected_game._get_nb_connected_player():
                player_id += 1
                selected_player = selected_game._get_connected_player()[player_id]._get_name_player()
                if player_pseudo_input == selected_player:
                    correct = True
            if correct:
                selected_game.remove_player_to_lobby(selected_player)
                """ ENVOYER '4' (requête quitter une partie reussit) AU DEMANDEUR """            
        else:
            """ ENVOYER '9' (requête quitter une partie echouée) AU DEMANDEUR """            

    def is_symbol_correct_request():
        pass

def main():
    pass

if __name__=='__main__':
    main()