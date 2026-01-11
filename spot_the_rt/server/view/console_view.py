class ConsoleView:
    def display_connection(self, client_address, client_username):
        """
        Affiche la connexion d un nouveau client
        """
        print(f"[+] Client connecté : {client_username} ({client_address})")
    
    def display_username_error(self, client_address, client_username, room_number):
        """
        Affiche une erreur de pseudo déjà utilisé
        """
        print(f"ERROR : Pseudo deja pris pour {client_address}")

    def display_message(self, client_address, client_username, room_number , message):
        """
        Affiche un message envoyé dans une room
        """
        print(f"ROOM {room_number} : {client_username} >> {message}")

    def display_message_test(self, message):
        """
        Affiche un message brut pour le debug
        """
        print(f"{message}")


    def display_disconnection(self, client_address, client_username):
        """
        Affiche la déconnexion d un client
        """
        print(f"[-] Client déconnecté : {client_address} alias {client_username}")

    ###

    def display_room_create(self, client_address, client_username, room_number):
        """
        Affiche la création d une room
        """
        print(f"ROOM {room_number} : [+] Creation d'une salle par {client_username}@{client_address}")

    def display_room_delete(self, client_address, client_username, room_number):
        """
        Affiche la suppression d une room
        """
        print(f"ROOM {room_number} : [-] Supression d'une salle par {client_username}@{client_address}")

    ###

    def display_room_join(self, client_address, client_username, room_number):
        """
        Affiche l entrée d un joueur dans une room
        """
        print(f"ROOM {room_number} : [+] Le joueur {client_username}@{client_address} a rejoins la room")

    def display_room_leave(self, client_address, client_username, room_number):
        """
        Affiche la sortie d un joueur d une room
        """
        print(f"ROOM {room_number} : [-] Le joueur {client_username}@{client_address} a quitté la room")

    def display_room_join_error(self, client_address, client_username, room_number):
        """
        Affiche une erreur lors de la tentative de rejoindre une room
        """
        print(f"ERROR : Le joueur {client_username}@{client_address} a essayé de se connecter à la room {room_number}")

    def display_room_launch(self, client_address, client_username, room_number):
        """
        Affiche le lancement d une partie
        """
        print(f"ROOM {room_number} : Lancement d'une partie par {client_username}@{client_address}")

    def display_room_launch_error(self, client_address, client_username, room_number):
        """
        Affiche une erreur de lancement par manque de joueurs
        """
        print(f"ERROR : Pas assez de joueurs sur la room {room_number} pour le lancement")

    def display_room_launch_error_arg(self, client_address, client_username, room_number):
        """
        Affiche une erreur de lancement sans nombre de rounds
        """
        print(f"ERROR : Le nombre de rounds n'est pas spécifié pour le lancement de la partie sur la room {room_number}")

    ###

    def display_symbol_verification(self, client_address, client_username, room_number, symbol, is_correct):
        """
        Affiche le résultat de la vérification d un symbole
        """
        if is_correct == "SYMBOL_ACK":
            print(f"ROOM {room_number} : Le joueur {client_username}@{client_address} a vérifié le symbole '{symbol}' : CORRECT")
        else:
            print(f"ROOM {room_number} : Le joueur {client_username}@{client_address} a vérifié le symbole '{symbol}' : INCORRECT")

    def display_symbol_verification_error_arg(self, client_address, client_username, room_number):
        """
        Affiche une erreur de vérification sans symbole
        """
        print(f"ERROR : Le joueur {client_username}@{client_address} a essayé de vérifier sans envoyé de symbole sur la room {room_number}")