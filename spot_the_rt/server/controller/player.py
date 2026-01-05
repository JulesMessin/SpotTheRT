class Player():

    def __init__(self, name_player:str = "Nolann", is_hostmaster:bool = False, id_affected_card:int = 1):
        self.__name_player = name_player
        self.__is_hostmaster = is_hostmaster
        self.__id_affected_card = id_affected_card

    def _get_name_player(self):
        return self.__name_player

    def _get_is_hostmaster(self):
        return self.__is_hostmaster

    def _get_id_affected_card(self):
        return self.__id_affected_card
    