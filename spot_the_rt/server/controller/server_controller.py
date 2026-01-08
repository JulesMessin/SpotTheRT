from urllib import request
from model.client_thread import ClientThread
from game_controller import GameController

class ServerController:
    def __init__(self, server_socket, view):
        self.server_socket = server_socket
        self.view = view
        self.clients = []
        self.game_controller = GameController()

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
                reply = self.game_controller.create_lobby_request(lobby_name_input=room_name, player_pseudo_input=client_username)
                new_message = f"client -room {room_name} -host {reply}"
                self.view.display_room_create(client_address, client_username, room_name)

                for thread in self.clients:
                    if thread.client_address == client_address:
                        new_message = new_message.encode('utf-8')
                        thread.client_socket.send(new_message)

            elif "-join" in parts:
                thread.room_name = room_name
                reply = self.game_controller.join_lobby_request(lobby_name_input=room_name, player_pseudo_input=client_username)
                new_message = f"client -room {room_name} -join {reply}"
                self.view.display_room_join(client_address, client_username, room_name)

                for thread in self.clients:
                    if thread.client_address == client_address:
                        new_message = new_message.encode('utf-8')
                        thread.client_socket.send(new_message)

            elif "-leave" in parts:
                thread.room_name = room_name
                reply = self.game_controller.quit_game_request(lobby_name_input=room_name, player_pseudo_input=client_username)
                new_message = f"client -room {room_name} -leave {reply}"
                self.view.display_room_leave(client_address, client_username, room_name)
                for thread in self.clients:
                    if thread.client_address == client_address:
                        thread.client_socket.send(new_message.encode('utf-8'))

            elif "-launch" in parts:
                thread.room_name = room_name
                try:
                    nb_round_index = parts.index("-launch") + 1
                    nb_round = parts[nb_round_index]
                    reply = self.game_controller.launch_game_request(lobby_name_input=room_name, player_pseudo_input=client_username, nb_round_input=nb_round)
                    new_message = f"client -room {room_name} -launch {reply}"
                    self.view.display_room_launch(client_address, client_username, room_name)

                except IndexError:
                    new_message = f"client -room {room_name} -launch LAUNCH_FAIL_NO_ROUND"
                    self.view.display_room_launch_error_arg(client_address, client_username, room_name)
                    return

                for thread in self.clients:
                    if thread.room_name == room_name:
                        thread.client_socket.send(new_message.encode('utf-8'))

            elif "-verify" in parts:
                thread.room_name = room_name
                try:
                    symbol_index = parts.index("-verify") + 1
                    symbol = parts[symbol_index]
                    reply = self.game_controller.is_symbol_correct_request(lobby_name_input=room_name, player_pseudo_input=client_username, symbol_input=symbol)
                    new_message = f"client -room {room_name} -verify {reply}"
                    self.view.display_symbol_verification(client_address, client_username, room_name, symbol, reply[0])

                except IndexError:
                    new_message = f"client -room {room_name} -verify VERIFY_FAIL_NO_SYMBOL"
                    self.view.display_symbol_verification_error_arg(client_address, client_username, room_name, "None", "VERIFY_FAIL_NO_SYMBOL")

                for thread in self.clients:
                    if thread.client_address == client_address:
                        thread.client_socket.send(new_message.encode('utf-8'))

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
