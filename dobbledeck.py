from random import randint, shuffle


class Dobbledeck:
    
    def __init__(self):
        pool_symbol = ['e', '8', 't', 'k', '0', 'J', 
                        'a', 'Z', 'G', 'F', 'v', '3', 
                        'E', 'b', '4', 's', 'L', 'T', 
                        'r', 'C', 'P', 'D', 'w', '9', 
                        'q', 'x', 'p', 'N', 'A', '1', 
                        'I', '5', 'Y', 'l', 'n', 'z']

        temp_pool = pool_symbol
        self.__common_card = []
        self.__card_player_1 = []
        self.__card_player_2 = []
        self.__card_player_3 = []
        self.__card_player_4 = []
        self.__card_player_5 = []
        self.__card_player_6 = []
        self.__card_player_7 = []
        self.__card_player_8 = []
        self.__list_cards = [
            self.__common_card, 
            self.__card_player_1, self.__card_player_2, self.__card_player_3, self.__card_player_4, 
            self.__card_player_5, self.__card_player_6, self.__card_player_7, self.__card_player_8]

        for card in range(9):
            for symbol in range(8-card):
                selected_symbol = randint(0, len(temp_pool)-1)
                self.__list_cards[card].append(temp_pool[selected_symbol])
                self.__list_cards[8 - symbol].append(temp_pool[selected_symbol])
                temp_pool.pop(selected_symbol)
            shuffle(self.__list_cards[card])
        self.__card_distributed = 0

    def _get_card(self, id_card):
        return self.__list_cards[id_card]

    def _set_card(self, old_card, new_card):
        old_card = new_card

    def generate_new_player_card(self, id_player_card):
        common_card = self.get_card(0)
        player_card = self.get_card(id_player_card)
        self._set_card(player_card, common_card)

    def generate_new_common_card(self):
        old_common_card = _get_card(0)
        new_common_card = []
        for card in range(1, 9):
            random_symbol = randint(0, 7)
            selected_card = self._get_card(card)
            new_common_card.append(selected_card[random_symbol])

        self._set_card(old_common_card, new_common_card)

    def give_card(self):
        pass

    def __str__(self):
        print(f"Carte Commune :     {self.__common_card}")
        print(f"Carte du Joueur 1 : {self.__card_player_1}")
        print(f"Carte du Joueur 2 : {self.__card_player_2}")
        print(f"Carte du Joueur 3 : {self.__card_player_3}")
        print(f"Carte du Joueur 4 : {self.__card_player_4}")
        print(f"Carte du Joueur 5 : {self.__card_player_5}")
        print(f"Carte du Joueur 6 : {self.__card_player_6}")
        print(f"Carte du Joueur 7 : {self.__card_player_7}")
        print(f"Carte du Joueur 8 : {self.__card_player_8}")
        return "Boujour"
    

def main():
    game_deck = Dobbledeck()
    print(game_deck)

    """
    Carte Commune :     ['q', 't', 'D', 'l', '0', 'F', 'w', 'J']
    Carte du Joueur 1 : ['3', 'P', 'e', 'C', '1', 'x', 'N', 'q']
    Carte du Joueur 2 : ['L', 'p', 'I', 'C', 's', 'A', 'G', '0']
    Carte du Joueur 3 : ['8', 'T', 'F', 'k', 'e', 'Y', 'L', 'Z']
    Carte du Joueur 4 : ['5', 'b', 't', 'p', 'N', 'T', 'v', '4']
    Carte du Joueur 5 : ['I', 'x', '8', '4', 'E', 'n', '9', 'w']
    Carte du Joueur 6 : ['r', 'b', 'a', 's', '9', 'P', 'Z', 'l']
    Carte du Joueur 7 : ['v', 'A', 'r', 'Y', 'D', '3', 'n', 'z']
    Carte du Joueur 8 : ['G', 'k', 'a', '5', 'E', 'J', '1', 'z']
    Boujour
    """


if __name__=="__main__":
    main()