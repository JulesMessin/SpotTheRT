from spot_the_rt import SpotTheRT


def main():
    spot_the_RT_game = SpotTheRT()
    while True:
        request = input("Requête : ")
        request.split(sep=",")
        print(request[0])
        if request[0]=="1":
            spot_the_RT_game.create_lobby_request(request)
        elif request[0]=="2":
            spot_the_RT_game.join_lobby_request(request)
        
        elif request[0]=="3":
            spot_the_RT_game.launch_game_request(request)
        elif request[0]=="4":
            spot_the_RT_game.quit_game_request(request)
        elif request[0]=="5":
            spot_the_RT_game.is_symbol_correct_request(request)
                

if __name__=='__main__':
    main()
