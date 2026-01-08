from game_controller import GameController


def main():
    spot_the_RT_game = GameController()

    """
    --- format des requetes clientes vers le serveur : 
    demande de creation de game :  <"CREATE", nom lobby, pseudo>
    demande de join une game :     <"JOIN", nom lobby, pseudo>
    demande de lancement de game : <"LAUNCH", nom lobby, pseudo, nb_round>
    demande de quitter le lobby :  <"EXIT", nom lobby, pseudo>
    demande de verif symbole :     <"VERIFY", nom lobby, pseudo, symbole>
    """

    while True:
        print("\nFormat requête : <type_requête>,<nom_lobby>,<pseudo_joueur>,<symbole>")
        request = input("Requête : ")
        request = request.split(",")


        if request[0]=="CREATE":
            reply = spot_the_RT_game.create_lobby_request(lobby_name_input=request[1], player_pseudo_input=request[2])
        elif request[0]=="JOIN":
            reply = spot_the_RT_game.join_lobby_request(lobby_name_input=request[1], player_pseudo_input=request[2])
        elif request[0]=="LAUNCH":
            reply = spot_the_RT_game.launch_game_request(lobby_name_input=request[1], player_pseudo_input=request[2], nb_round_input=request[3])
        elif request[0]=="EXIT":
            reply = spot_the_RT_game.quit_game_request(lobby_name_input=request[1], player_pseudo_input=request[2])
        elif request[0]=="VERIFY":
            reply = spot_the_RT_game.is_symbol_correct_request(lobby_name_input=request[1], player_pseudo_input=request[2], symbol_input=request[3])


if __name__=='__main__':
    main()
