from dobbledeck import Dobbledeck
from game import Game


class Player(Dobbledeck):

    def __init__(self, name_player:str = "Nolann", is_hostmaster:bool = False, id_affected_card:int = 1):
        self.__name_player = name_player
        self.__is_hostname = is_hostname
        self.__id_affected_card = id_affected_card
    