from player import Player
from dobbledeck import Dobbledeck


class Game():

    def __init__(self, nb_round:int = 47, connected_player:dict = {}, lobby_name:str = "Partie") -> None:
        self.__nb_round = nb_round
        self.__connected_player = connected_player
        self.__lobby_name = lobby_name
        self.__game_deck = Dobbledeck()

    def _set_nb_round(self, new_nb_round:int) -> None:
        self.__nb_round = new_nb_round

    def _add_connected_player(self, new_connected_player_name:str, new_connected_player:object) -> None:
        self.__connected_player[new_connected_player_name] = new_connected_player

    def _del_connected_player(self, connected_player_name:str) -> None:
        self.__connected_player.pop(connected_player_name)

    def _get_nb_round(self) -> int:
        return self.__nb_round

    def _get_connected_player(self) -> dict:
        return self.__connected_player

    def _get_lobby_name(self) -> str:
        return self.__lobby_name

    def _get_game_deck(self) -> object:
        return self.__game_deck

    def add_player_to_lobby(self, new_player_name:str, new_player_status:bool) -> None:
        new_player_card_id = len(self._get_connected_player()) + 1
        new_player = Player(name_player=new_player_name, is_hostmaster=new_player_status, id_affected_card=new_player_card_id)
        self._add_connected_player(new_connected_player_name=new_player_name, new_connected_player=new_player)

    def remove_player_to_lobby(self, player_name_input:object) -> None:
        self._del_connected_player(connected_player_name=player_name_input)

    def __str__(self):
        return f"Liste des Joueurs dans la partie {self._get_lobby_name()} :\n{self._get_connected_player()}"

# Test du code
def main():
    game_test = Game(lobby_name="TestLobby")
    game_test.add_player_to_lobby(new_player_name="Alice", new_player_status=True)
    game_test.add_player_to_lobby(new_player_name="Bob", new_player_status=False)
    print(game_test)

if __name__=='__main__':
    main()


"""
Liste des Joueurs dans la partie TestLobby :
{'Alice': <player.Player object at 0x0000016455E39160>, 'Bob': <player.Player object at 0x0000016455D57390>}

"""