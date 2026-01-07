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

        #self.view.display_message_test(message) #pour tester

        thread = next((c for c in self.clients if c.client_address == client_address), None)
        if not thread:
            return

        parts = message.split()
        if len(parts) == 0:
            return
        # commande
        
        if parts[0] == "server" and "-room" in parts:
            try:
                room_index = parts.index("-room") + 1
                room_name = parts[room_index]
            except IndexError:
                print("Erreur : nom de room manquant")
                return

            if "-host" in parts:
                thread.room_name = room_name
                #spot_the_RT_game.create_lobby_request(lobby_name_input=request[1], player_pseudo_input=request[2])
                new_message = f"client -room {room_name} -host"
                self.view.display_room_create(client_address, client_username, room_name)

                for thread in self.clients:
                    if thread.client_address == client_address:
                        new_message = new_message.encode('utf-8')
                        thread.client_socket.send(new_message)

            elif "-join" in parts:
                thread.room_name = room_name
                #spot_the_RT_game.create_lobby_request(lobby_name_input=request[1], player_pseudo_input=request[2])
                new_message = f"client -room {room_name} -join"
                self.view.display_room_join(client_address, client_username, room_name)

                for thread in self.clients:
                    if thread.client_address == client_address:
                        new_message = new_message.encode('utf-8')
                        thread.client_socket.send(new_message)

            elif "-leave" in parts:
                #spot_the_RT_game.create_lobby_request(lobby_name_input=request[1], player_pseudo_input=request[2])
                new_message = f"client -room {room_name} -leave"
                self.view.display_room_leave(client_address, client_username, room_name)

                for thread in self.clients:
                    if thread.client_address == client_address:
                        new_message = new_message.encode('utf-8')
                        thread.client_socket.send(new_message)

            elif "-launch" in parts:
                #spot_the_RT_game.create_lobby_request(lobby_name_input=request[1], player_pseudo_input=request[2])
                new_message = f"client -room {room_name} -launch"
                self.view.display_room_launch(client_address, client_username, room_name)

                for thread in self.clients:
                    if thread.room_name == room_name:
                        thread.client_socket.send(f"client -room {room_name} -launch".encode('utf-8'))

            elif "-chat" in parts:
                chat_index = parts.index("-chat") + 1
                chat_message = " ".join(parts[chat_index:])
                for thread in self.clients:
                    if thread.room_name == room_name: 
                        thread.client_socket.send(f"client -room {room_name} -chat {client_username} : {chat_message}".encode("utf-8"))
                self.view.display_message(client_address, client_username, room_name, chat_message)


    def client_disconnected(self, client_address, client_username):
        self.clients = [t for t in self.clients if t.client_address != client_address]
        self.view.display_disconnection(client_address,client_username)
