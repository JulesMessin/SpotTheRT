from random import randint, shuffle


class Dobbledeck:
    
    def __init__(self) -> None:
        pool_symbol = ['antene', 'arduino', 'binaire', 'bluetooth', 'C++', 'cartemere', 
                        'casque', 'cisco', 'clavier', 'cloud', 'cmd', 'commutateur', 
                        'docker', 'electrique', 'firewall', 'github', 'goofyphone', 'laptop', 
                        'linux', 'logo', 'manette', 'onde', 'pc', 'php', 
                        'proxmox', 'python', 'raspberry_pi', 'rj45', 'robot', 'routeur', 
                        'satellite', 'souris', 'telephone', 'web', 'wifi', 'windows']
        
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

    def _get_list_cards(self) -> list:
        return self.__list_cards

    def _get_card(self, id_card:int) -> list:
        return self.__list_cards[id_card]

    def _set_card(self, old_card:list, new_card:list) -> None:
        old_card.clear()
        old_card.extend(new_card)

    def give_new_player_card(self, id_player_card:int) -> None:
        common_card = self._get_card(0)
        player_card = self._get_card(id_player_card)
        self._set_card(old_card=player_card, new_card=common_card)

    def generate_new_common_card(self) -> None:
        old_common_card = self._get_card(0)
        new_common_card = []
        for card in range(1, 9):
            random_symbol = randint(0, 7)
            selected_card = self._get_card(card)
            new_common_card.append(selected_card[random_symbol])
        self._set_card(old_card=old_common_card, new_card=new_common_card)

    def __str__(self) -> str:
        return f"Carte Commune :     {self._get_list_cards()[0]}\nCarte du Joueur 1 : {self._get_list_cards()[1]}\nCarte du Joueur 2 : {self._get_list_cards()[2]}\nCarte du Joueur 3 : {self._get_list_cards()[3]}\nCarte du Joueur 4 : {self._get_list_cards()[4]}\nCarte du Joueur 5 : {self._get_list_cards()[5]}\nCarte du Joueur 6 : {self._get_list_cards()[6]}\nCarte du Joueur 7 : {self._get_list_cards()[7]}\nCarte du Joueur 8 : {self._get_list_cards()[8]}\n\n--Liste : {self._get_list_cards()}--\n"

# Test du code
def main():
    deck_test = Dobbledeck()
    print(deck_test)
    
    deck_test.give_new_player_card(id_player_card=2)
    print("Nouvelle carte joueur 2 générée")
    print(deck_test)

    deck_test.generate_new_common_card()
    print("1ère Nouvelle carte commune générée")
    print(deck_test)

    deck_test.give_new_player_card(id_player_card=7)
    print("Nouvelle carte joueur 7 générée")
    print(deck_test)

    deck_test.generate_new_common_card()
    print("2ème Nouvelle carte commune générée")
    print(deck_test)


if __name__=='__main__':
    main()


"""

Carte Commune :     ['cloud', 'cmd', 'routeur', 'robot', 'proxmox', 'manette', 'binaire', 'telephone']
Carte du Joueur 1 : ['windows', 'github', 'rj45', 'arduino', 'electrique', 'web', 'cmd', 'commutateur']
Carte du Joueur 2 : ['raspberry_pi', 'linux', 'casque', 'electrique', 'firewall', 'cloud', 'cisco', 'pc']
Carte du Joueur 3 : ['clavier', 'github', 'php', 'proxmox', 'python', 'docker', 'casque', 'antene']
Carte du Joueur 4 : ['web', 'python', 'telephone', 'onde', 'souris', 'raspberry_pi', 'wifi', 'satellite']
Carte du Joueur 5 : ['manette', 'antene', 'bluetooth', 'cisco', 'windows', 'laptop', 'cartemere', 'wifi']
Carte du Joueur 6 : ['binaire', 'logo', 'pc', 'clavier', 'laptop', 'commutateur', 'goofyphone', 'souris']
Carte du Joueur 7 : ['php', 'rj45', 'C++', 'cartemere', 'goofyphone', 'satellite', 'routeur', 'firewall']
Carte du Joueur 8 : ['arduino', 'robot', 'docker', 'C++', 'logo', 'onde', 'bluetooth', 'linux']

Nouvelle carte joueur 2 générée
Carte Commune :     ['cloud', 'cmd', 'routeur', 'robot', 'proxmox', 'manette', 'binaire', 'telephone']
Carte du Joueur 1 : ['windows', 'github', 'rj45', 'arduino', 'electrique', 'web', 'cmd', 'commutateur']
Carte du Joueur 2 : ['cloud', 'cmd', 'routeur', 'robot', 'proxmox', 'manette', 'binaire', 'telephone']
Carte du Joueur 3 : ['clavier', 'github', 'php', 'proxmox', 'python', 'docker', 'casque', 'antene']
Carte du Joueur 4 : ['web', 'python', 'telephone', 'onde', 'souris', 'raspberry_pi', 'wifi', 'satellite']
Carte du Joueur 5 : ['manette', 'antene', 'bluetooth', 'cisco', 'windows', 'laptop', 'cartemere', 'wifi']
Carte du Joueur 6 : ['binaire', 'logo', 'pc', 'clavier', 'laptop', 'commutateur', 'goofyphone', 'souris']
Carte du Joueur 7 : ['php', 'rj45', 'C++', 'cartemere', 'goofyphone', 'satellite', 'routeur', 'firewall']
Carte du Joueur 8 : ['arduino', 'robot', 'docker', 'C++', 'logo', 'onde', 'bluetooth', 'linux']

1ère Nouvelle carte commune générée
Carte Commune :     ['cmd', 'routeur', 'proxmox', 'telephone', 'cisco', 'clavier', 'C++', 'bluetooth']
Carte du Joueur 1 : ['windows', 'github', 'rj45', 'arduino', 'electrique', 'web', 'cmd', 'commutateur']
Carte du Joueur 2 : ['cloud', 'cmd', 'routeur', 'robot', 'proxmox', 'manette', 'binaire', 'telephone']
Carte du Joueur 3 : ['clavier', 'github', 'php', 'proxmox', 'python', 'docker', 'casque', 'antene']
Carte du Joueur 4 : ['web', 'python', 'telephone', 'onde', 'souris', 'raspberry_pi', 'wifi', 'satellite']
Carte du Joueur 5 : ['manette', 'antene', 'bluetooth', 'cisco', 'windows', 'laptop', 'cartemere', 'wifi']
Carte du Joueur 6 : ['binaire', 'logo', 'pc', 'clavier', 'laptop', 'commutateur', 'goofyphone', 'souris']
Carte du Joueur 7 : ['php', 'rj45', 'C++', 'cartemere', 'goofyphone', 'satellite', 'routeur', 'firewall']
Carte du Joueur 8 : ['arduino', 'robot', 'docker', 'C++', 'logo', 'onde', 'bluetooth', 'linux']

Nouvelle carte joueur 7 générée
Carte Commune :     ['cmd', 'routeur', 'proxmox', 'telephone', 'cisco', 'clavier', 'C++', 'bluetooth']
Carte du Joueur 1 : ['windows', 'github', 'rj45', 'arduino', 'electrique', 'web', 'cmd', 'commutateur']
Carte du Joueur 2 : ['cloud', 'cmd', 'routeur', 'robot', 'proxmox', 'manette', 'binaire', 'telephone']
Carte du Joueur 3 : ['clavier', 'github', 'php', 'proxmox', 'python', 'docker', 'casque', 'antene']
Carte du Joueur 4 : ['web', 'python', 'telephone', 'onde', 'souris', 'raspberry_pi', 'wifi', 'satellite']
Carte du Joueur 5 : ['manette', 'antene', 'bluetooth', 'cisco', 'windows', 'laptop', 'cartemere', 'wifi']
Carte du Joueur 6 : ['binaire', 'logo', 'pc', 'clavier', 'laptop', 'commutateur', 'goofyphone', 'souris']
Carte du Joueur 7 : ['cmd', 'routeur', 'proxmox', 'telephone', 'cisco', 'clavier', 'C++', 'bluetooth']
Carte du Joueur 8 : ['arduino', 'robot', 'docker', 'C++', 'logo', 'onde', 'bluetooth', 'linux']

2ème Nouvelle carte commune générée
Carte Commune :     ['arduino', 'cloud', 'python', 'web', 'windows', 'goofyphone', 'bluetooth', 'robot']
Carte du Joueur 1 : ['windows', 'github', 'rj45', 'arduino', 'electrique', 'web', 'cmd', 'commutateur']
Carte du Joueur 2 : ['cloud', 'cmd', 'routeur', 'robot', 'proxmox', 'manette', 'binaire', 'telephone']
Carte du Joueur 3 : ['clavier', 'github', 'php', 'proxmox', 'python', 'docker', 'casque', 'antene']
Carte du Joueur 4 : ['web', 'python', 'telephone', 'onde', 'souris', 'raspberry_pi', 'wifi', 'satellite']
Carte du Joueur 5 : ['manette', 'antene', 'bluetooth', 'cisco', 'windows', 'laptop', 'cartemere', 'wifi']
Carte du Joueur 6 : ['binaire', 'logo', 'pc', 'clavier', 'laptop', 'commutateur', 'goofyphone', 'souris']
Carte du Joueur 7 : ['cmd', 'routeur', 'proxmox', 'telephone', 'cisco', 'clavier', 'C++', 'bluetooth']
Carte du Joueur 8 : ['arduino', 'robot', 'docker', 'C++', 'logo', 'onde', 'bluetooth', 'linux']
"""