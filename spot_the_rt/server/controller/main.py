from spot_the_rt import SpotTheRT


def main():
    spot_the_RT_game = SpotTheRT()
    while True:
        print("\nFormat requête : <type_requête>,<nom_lobby>,<pseudo_joueur>,<symbole>")
        request = input("Requête : ")
        request = request.split(",")
        print(request[0])
        print(request[1])
        print(request[2])
        print(request[3] if len(request) > 3 else "No symbol")

        if request[0]=="1":
            spot_the_RT_game.create_lobby_request(lobby_name_input=request[1], player_pseudo_input=request[2])
        elif request[0]=="2":
            spot_the_RT_game.join_lobby_request(lobby_name_input=request[1], player_pseudo_input=request[2])
        elif request[0]=="3":
            spot_the_RT_game.launch_game_request(lobby_name_input=request[1])
        elif request[0]=="4":
            spot_the_RT_game.quit_game_request(lobby_name_input=request[1], player_pseudo_input=request[2])
        elif request[0]=="5":
            spot_the_RT_game.is_symbol_correct_request(lobby_name_input=request[1], player_pseudo_input=request[2], symbol_input=request[3])


if __name__=='__main__':
    main()
