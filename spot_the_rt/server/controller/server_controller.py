from model.client_thread import ClientThread

class ServerController:
    def __init__(self, server_socket, view):
        self.server_socket = server_socket
        self.view = view
        self.clients = []

    def accept_connections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            try:
                client_username = client_socket.recv(1024).decode("utf-8")   
            except Exception:
                client_username = "Inconnu"
                
            thread = ClientThread(client_socket, client_address, client_username, self)
            self.clients.append(thread)
            thread.start()
            self.view.display_connection(client_address, client_username)

    def handle_message(self, client_address, client_username, message):
        self.view.display_message(client_address, client_username ,message)
        new_message = ""
        # commande
        if message.startswith("void"):
            parts = message.split()
            if len(parts) == 0:
                return

            sender = parts[0]

            if "-setbackground" in parts:
                try:
                    color_index = parts.index("-setbackground") + 1
                    color = parts[color_index]
                    new_message = f"void -setbackground {color}"
                except IndexError:
                    new_message = "Erreur : couleur manquante"


            if "-all" in parts:
                for thread in self.clients:
                    thread.client_socket.send(new_message.encode("utf-8"))
                return
            else:
                for thread in self.clients:
                        if thread.client_address == client_address:
                            new_message = new_message.encode('utf-8')
                            thread.client_socket.send(new_message)
                            break
        
        elif message.startswith("game"):
            parts = message.split()
            if len(parts) == 0:
                return

            sender = parts[0]

            if "-create" in parts:
                try:
                    spot_the_RT_game.create_lobby_request(lobby_name_input=request[1], player_pseudo_input=request[2])

            elif "-join" in parts:
                try:
                    spot_the_RT_game.join_lobby_request(lobby_name_input=request[1], player_pseudo_input=request[2])

            elif "-launch" in parts:
                try:
                   spot_the_RT_game.launch_game_request(lobby_name_input=request[1])


            elif "-quit" in parts:
                try:
                    spot_the_RT_game.quit_game_request(lobby_name_input=request[1], player_pseudo_input=request[2])


            elif "-check" in parts:
                try:
                    spot_the_RT_game.is_symbol_correct_request(lobby_name_input=request[1], player_pseudo_input=request[2], symbol_input=request[3])
                          

        
        # message
        else:
            new_message = f"{client_username} : {message}"
            new_message = new_message.encode('utf-8')
            for thread in self.clients:
                    thread.client_socket.send(new_message)

        self.view.display_message(client_address, client_username, new_message)


    def client_disconnected(self, client_address, client_username):
        self.clients = [t for t in self.clients if t.client_address != client_address]
        self.view.display_disconnection(client_address,client_username)
