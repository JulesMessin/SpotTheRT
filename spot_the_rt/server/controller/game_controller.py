from controller.game import Game


class GameController:

    def __init__(self, dict_game:dict = {}) -> None:
        self.__dict_game = dict_game

    def _add_game(self, lobby_name_input:str, new_game_input:object) -> None:
        self.__dict_game[lobby_name_input] = new_game_input

    def _get_dict_game(self) -> dict:
        return self.__dict_game

    def create_lobby_request(self, lobby_name_input:str, player_pseudo_input:str):

        # Verifier si le nom du lobby n'existe pas déjà
        if not lobby_name_input in self._get_dict_game().keys():
            # Créer la nouvelle partie, l'ajouter au dictionnaire et ajouter le joueur en tant qu'hostmaster
            new_game = Game(lobby_name=lobby_name_input)
            self._add_game(lobby_name_input=lobby_name_input, new_game_input=new_game)
            new_game.add_player_to_lobby(new_player_name=player_pseudo_input, new_player_status=True)
            return "CREATE_ACK"
        else:
            # Lobby déjà existant
            return "CREATE_FAIL"
            
    def join_lobby_request(self, lobby_name_input:str, player_pseudo_input:str):

        # Verifier si le nom du lobby n'existe pas déjà
        if lobby_name_input in self._get_dict_game().keys():
            selected_game = self._get_dict_game()[lobby_name_input]

            # Verifier si la partie n'est pas pleine
            if len(selected_game._get_connected_player()) < 8:

                # Verifier si le pseudo n'est pas déjà pris
                if not player_pseudo_input in selected_game._get_connected_player().keys():
                    # Ajouter le joueur à la partie
                    selected_game.add_player_to_lobby(new_player_name=player_pseudo_input, new_player_status=False)
                    return "JOIN_ACK", selected_game._get_connected_player().keys()
                else:
                    # Pseudo déjà pris
                    return "JOIN_FAIL_PSEUDO"
            else:
                # Lobby plein
                return "JOIN_FAIL_LOBBY_FULL"
        else:
            # Lobby non trouvé
            return "JOIN_FAIL_NO_LOBBY"
            
    def launch_game_request(self, lobby_name_input:str, player_pseudo_input:str, nb_round_input:int):

        # Verifier si le nom du lobby n'existe pas déjà
        if lobby_name_input in self._get_dict_game().keys():
            selected_game = self._get_dict_game()[lobby_name_input]

            # Verifier si le joueur est bien dans la partie
            if  player_pseudo_input in selected_game._get_connected_player().keys():

                # Verifier si le joueur est l'hostmaster
                if selected_game._get_connected_player()[player_pseudo_input]._get_is_hostmaster():

                    # Verifier si il y a assez de joueurs (> 2) pour lancer la partie
                    if len(selected_game._get_connected_player()) >= 2:
                        # Lancer la partie
                        selected_game._set_nb_round(new_nb_round=nb_round_input)
                        return "LAUNCH_ACK", selected_game._get_game_deck()._get_list_cards()
                    else:
                        # Lobby pas assez rempli
                        return "LAUNCH_FAIL_NOT_ENOUGH_PLAYER"
                else:
                    # Joueur n'est pas l'hostmaster
                    return "LAUNCH_FAIL_NOT_HOST"
            else:
                # Joueur non trouvé
                return "LAUNCH_FAIL_NO_PLAYER"
        else:
            # Lobby non trouvé
            return "LAUNCH_FAIL_NO_LOBBY"

    def quit_game_request(self, lobby_name_input:str, player_pseudo_input:str) -> None:
        
        # Verifier si le nom du lobby n'existe pas déjà
        if lobby_name_input in self._get_dict_game().keys():
            selected_game = self._get_dict_game()[lobby_name_input]

            # Verifier si le joueur est bien dans la partie
            if player_pseudo_input in selected_game._get_connected_player().keys():
                # Supprimer le joueur de la partie verifier si la partie est vide, si oui la supprimer
                selected_game.remove_player_to_lobby(player_name_input=player_pseudo_input)
                if len(selected_game._get_connected_player()) == 0:
                    self._get_dict_game().pop(lobby_name_input)
                return "EXIT_ACK"
            else:
                # Joueur non trouvé
                return "EXIT_FAIL_NO_PLAYER"
        else:
            # Lobby non trouvé
            return "EXIT_FAIL_NO_LOBBY"
            
    def is_symbol_correct_request(self, lobby_name_input:str, player_pseudo_input:str, symbol_input:str) -> None:
        
        # Verifier si le nom du lobby n'existe pas déjà
        if lobby_name_input in self._get_dict_game().keys():
            selected_game = self._get_dict_game()[lobby_name_input]

            # Verifier si le joueur est bien dans la partie
            if player_pseudo_input in selected_game._get_connected_player().keys():
                selected_common_card = selected_game._get_game_deck()._get_card(0)
                id_card_player = selected_game._get_connected_player()[player_pseudo_input]._get_id_affected_card()
                selected_player_card = selected_game._get_game_deck()._get_card(id_card_player)
                
                # Vérifier si le symbole est présent dans la carte commune et dans la carte du joueur
                if symbol_input in selected_common_card and symbol_input in selected_player_card:
                    # Donner la carte commune au joueur
                    id_player_card = selected_game._get_connected_player()[player_pseudo_input]._get_id_affected_card()
                    selected_game._get_game_deck().give_new_player_card(id_player_card=id_player_card)

                    # Générer une nouvelle carte commune
                    selected_game._get_game_deck().generate_new_common_card()

                    # Incrémenter le score du joueur
                    new_player_point = selected_game._get_connected_player()[player_pseudo_input]._get_player_point() + 1
                    selected_game._get_connected_player()[player_pseudo_input]._set_player_point(new_player_point=new_player_point)

                    # Décrémenter le nombre de round restant                    
                    new_nb_round = int(selected_game._get_nb_round()) - 1
                    selected_game._set_nb_round(new_nb_round=new_nb_round)

                    # Vérifier si la partie est terminée
                    if selected_game._get_nb_round() == 0:
                        # Fin de la partie
                        # Trouver le gagnant en trouvant le score le plus élevé et le joueur associé
                        list_point = []
                        for p in selected_game._get_connected_player().values():
                            list_point.append(p._get_player_point())
                        max_point = max(list_point)

                        for key, player in selected_game._get_connected_player().items():
                            if player._get_player_point() == max_point:
                                winner_player_name = key
                                winner_player_point = player._get_player_point()

                        # Supprimer la partie du dictionnaire
                        self._get_dict_game().pop(lobby_name_input)

                        return "GAME_OVER", winner_player_name, winner_player_point
                    else:
                        # Symbole correct, continuer la partie
                        return "SYMBOL_ACK", selected_game._get_game_deck()._get_list_cards(), selected_game._get_connected_player()[player_pseudo_input]._get_player_point(), selected_game._get_nb_round()
                else:
                    # Symbole incorrect
                    return "SYMBOL_FAIL"
            else:
                # Joueur non trouvé
                return "SYMBOL_FAIL_NO_PLAYER"
        else:
            # Lobby non trouvé
            return "SYMBOL_FAIL_NO_LOBBY"