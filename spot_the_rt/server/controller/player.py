class Player():

    def __init__(self, name_player:str = "Nolann", is_hostmaster:bool = False, id_affected_card:int = 0, player_point:int = 0) -> None:
        self.__name_player = name_player
        self.__is_hostmaster = is_hostmaster
        self.__id_affected_card = id_affected_card
        self.__player_point = player_point

    def _get_name_player(self) -> str:
        return self.__name_player

    def _get_is_hostmaster(self) -> bool:
        return self.__is_hostmaster

    def _get_id_affected_card(self) -> int:
        return self.__id_affected_card
    
    def _get_player_point(self) -> int:
        return self.__player_point
    
    def _set_id_affected_card(self, new_id_affected_card:int) -> None:
        self.__id_affected_card = new_id_affected_card
    
    def _set_player_point(self, new_player_point:int) -> None:
        self.__player_point = new_player_point
    
    def __str__(self):
        return f"Info sur le joueur {self._get_name_player()} : host({self._get_is_hostmaster()}) ; nombre de point({self._get_player_point()})"


# Test du code
def main():
    player_test = Player(name_player="Alice", is_hostmaster=True, id_affected_card=1)
    print(player_test)

if __name__=='__main__':
    main()


"""

Info sur le joueur Alice : host(True) ; nombre de point(0)

"""