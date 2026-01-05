from dobbledeck import Dobbledeck
from game import Game
from player import Player

class SpotTheRT:

    def __init__(self, dict_game:dict = {}) -> None:
        self.__dict_game = dict_game

    def _add_game(self, lobby_name_input:str, new_game_input:object) -> None:
        self.__dict_game[lobby_name_input] = new_game_input

    def _get_dict_game(self) -> dict:
        return self.__dict_game

    def create_lobby_request(self, lobby_name_input:str, player_pseudo_input:str) -> None:
        if not lobby_name_input in self._get_dict_game().keys():
            new_game_id = len(self._get_dict_game()) + 1
            new_game = Game(lobby_name=lobby_name_input, game_id=new_game_id)
            self._add_game(lobby_name_input=lobby_name_input, new_game_input=new_game)
            new_game.add_player_to_lobby(new_player_name=player_pseudo_input, new_player_status=True)
            print(" ENVOYER '1' (requête créer un lobby reussit) AU DEMANDEUR ")
            """ ENVOYER '1' (requête créer un lobby reussit) AU DEMANDEUR """
        else:
            print("ENVOYER '6' (requête créer un lobby echouée) AU DEMANDEUR")
            """ ENVOYER '6' (requête créer un lobby echouée) AU DEMANDEUR """

    def join_lobby_request(self, lobby_name_input:str, player_pseudo_input:str) -> None:
        if lobby_name_input in self._get_dict_game().keys():
            selected_game = self._get_dict_game()[lobby_name_input]
            if not player_pseudo_input in selected_game._get_connected_player().keys():
                selected_game.add_player_to_lobby(new_player_name=player_pseudo_input, new_player_status=False)
                print("ENVOYER '2' (requête rejoindre un lobby reussit) AU DEMANDEUR")
                """ ENVOYER '2' (requête rejoindre un lobby reussit) AU DEMANDEUR """
            else:
                print("ENVOYER '72' (requête rejoindre un lobby echouée, pseudo déjà utilisé) AU DEMANDEUR")
                """ ENVOYER '72' (requête rejoindre un lobby echouée, pseudo déjà utilisé) AU DEMANDEUR """
        else:
            print("ENVOYER '71' (requête rejoindre un lobby echouée, lobby inexistant) AU DEMANDEUR")
            """ ENVOYER '71' (requête rejoindre un lobby echouée, lobby inexistant) AU DEMANDEUR """

    def launch_game_request(self, lobby_name_input:str, player_pseudo_input:str) -> None:
        if lobby_name_input in self._get_dict_game().keys():
            selected_game = self._get_dict_game()[lobby_name_input]
            if selected_game._get_connected_player()[player_pseudo_input]._get_is_hostmaster():
                if len(selected_game._get_connected_player()) >= 2:
                    for player_id in range(1, len(selected_game._get_connected_player()) + 1):
                        requested_common_card = selected_game._get_game_deck()._get_card(id_card=0)
                        requested_player_card = selected_game._get_game_deck()._get_card(id_card=player_id)
                        print(f"JOUEUR ID {player_id} - CARTE COMMUNE : {requested_common_card} - CARTE JOUEUR : {requested_player_card}")
                    print("ENVOYER '3'  (lancer une partie reussi) et LES CARTES AU JOUEUR SELON 'player_id'")
                    """ ENVOYER '3'  (lancer une partie reussi) et LES CARTES AU JOUEUR SELON 'player_id' """
                else:
                    print("ENVOYER '82' (requête lancer une partie echouée, pas assez de joueurs) AU DEMANDEUR")
                    """ ENVOYER '82' (requête lancer une partie echouée, pas assez de joueurs) AU DEMANDEUR """
            else:
                print("ENVOYER '83' (requête lancer une partie echouée, joueur non hostmaster) AU DEMANDEUR")
                """ ENVOYER '83' (requête lancer une partie echouée, joueur non hostmaster) AU DEMANDEUR """
        else:
            print("ENVOYER '81' (requête lancer une partie echouée, partie inexistante) AU DEMANDEUR")
            """ ENVOYER '81' (requête lancer une partie echouée, partie inexistante) AU DEMANDEUR """

    def quit_game_request(self, lobby_name_input:str, player_pseudo_input:str) -> None:
        if lobby_name_input in self._get_dict_game().keys():
            selected_game = self._get_dict_game()[lobby_name_input]
            if  player_pseudo_input in selected_game._get_connected_player().keys():
                selected_game.remove_player_to_lobby(player_name_input=player_pseudo_input)
                if len(selected_game._get_connected_player()) == 0:
                    self._get_dict_game().pop(lobby_name_input)
                print("ENVOYER '4' (requête quitter une partie reussit) AU DEMANDEUR")
                """ ENVOYER '4' (requête quitter une partie reussit) AU DEMANDEUR """  
            else:
                print("ENVOYER '92' (requête quitter une partie echouée, joueur inexistant) AU DEMANDEUR")
                """ ENVOYER '92' (requête quitter une partie echouée, joueur inexistant) AU DEMANDEUR """          
        else:
            print("ENVOYER '91' (requête quitter une partie echouée) AU DEMANDEUR")
            """ ENVOYER '91' (requête quitter une partie echouée) AU DEMANDEUR """            

    def is_symbol_correct_request(self, lobby_name_input:str, player_pseudo_input:str, symbol_input:str) -> None:
        if lobby_name_input in self._get_dict_game().keys():
            selected_game = self._get_dict_game()[lobby_name_input]
            selected_common_card = selected_game._get_game_deck()._get_card(0)
            try:
                selected_symbol = selected_common_card.index(symbol_input)

                id_player_card = selected_game._get_connected_player()[player_pseudo_input]._get_player_card_id()
                selected_game._get_game_deck().generate_new_player_card(id_player_card=id_player_card)
                selected_game._get_game_deck().generate_new_common_card()
                print(f"New Common Card : {selected_game._get_game_deck()._get_card(0)}")
                print(f"New Player Card : {selected_game._get_game_deck()._get_card(id_player_card)}")
                print("ENVOYER '50' (requête verif self symbole bon) AU DEMANDEUR")
                print("ENVOYER '52' (requête verif symbole adversaire bon) AUX AUTRES")
                """ ENVOYER '50' (requête verif self symbole bon) AU DEMANDEUR """
                """ ENVOYER '52' (requête verif symbole adversaire bon) AUX AUTRES """
            except ValueError:
                print("ENVOYER '51' (requête verif self symbole mauvais) AU DEMANDEUR")
                """ ENVOYER '51' (requête verif self symbole mauvais) AU DEMANDEUR """
