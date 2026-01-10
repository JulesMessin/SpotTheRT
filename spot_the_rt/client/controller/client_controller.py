from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
import socket

class ReceiveThread(QThread):
    message_received = pyqtSignal(str)

    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket
        self.running = True

    def run(self):
        while self.running:
            try:
                data = self.client_socket.recv(1024)
                if data:
                    message = data.decode("utf-8")
                    self.message_received.emit(message)
                else:
                    break
            except Exception:
                break

    def stop(self):
        self.running = False
        self.client_socket.close()


class ClientController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.receive_thread = None
        self.current_room = None

    def connect_to_server(self, ip, port, message_callback, status_callback, username):
        try:
            self.model.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.model.client_socket.connect((ip, port))
            self.model.client_socket.send(username.encode("utf-8"))
            self.model.connected = True
            
            status_callback(f"Connecté à {ip}:{port} en tant que {username}")
            
            self.receive_thread = ReceiveThread(self.model.client_socket)
            self.receive_thread.message_received.connect(self.handle_message)
            self.receive_thread.start()
        except Exception as e:
            status_callback("Statut : erreur de connexion")
            raise e



    def handle_message(self, message):
            print(message)
            parts = message.split()

            if not parts:
                return

            if parts[0] == "client" and "-room" in parts:
                try:
                    room_index = parts.index("-room") + 1
                    room_name = parts[room_index]
                except IndexError:
                    return

                if "-host" in parts:
                    create_index = parts.index("-host") + 1
                    host_response = parts[create_index]
                    if host_response == "CREATE_ACK":
                        self.join_waiting_room(username=self.view.username_field.text(),
                                               room_name=room_name,
                                               is_host=True)
                    elif host_response == "CREATE_FAIL":
                        self.back_to_start_view(error_message="Erreur : le nom de la room est déjà pris.", 
                                                username=self.view.username_field.text(), 
                                                room_name=room_name)
                        
                    print("host")
                    self.current_room = room_name

                elif "-join" in parts:
                    join_index = parts.index("-join") + 1
                    join_response = parts[join_index]
                    if join_response == "JOIN_ACK":
                        self.join_waiting_room(username=self.view.username_field.text(),
                                               room_name=room_name,
                                               is_host=False)
                    elif join_response == "JOIN_FAIL_PSEUDO":
                        self.back_to_start_view(error_message="Erreur : le pseudo est déjà pris dans cette room.", 
                                                username=self.view.username_field.text(),
                                                room_name=room_name)
                    elif join_response == "JOIN_FAIL_LOBBY_FULL":
                        self.back_to_start_view(error_message="Erreur : la room est pleine.", 
                                                username=self.view.username_field.text(),
                                                room_name=room_name)
                    elif join_response == "JOIN_FAIL_NO_LOBBY":
                        self.back_to_start_view(error_message="Erreur : la room n'existe pas.", 
                                                username=self.view.username_field.text(),
                                                room_name=room_name)
                    print("join")
                    self.current_room = room_name

                elif "-launch" in parts:
                    launch_index = parts.index("-launch") + 1
                    launch_response = parts[launch_index]

                    print(launch_response)
                    

                    if launch_response == "LAUNCH_ACK":
                        self.show_game_room(username=self.view.username_field.text(),
                                            room_name=room_name, 
                                            nb_round=self.view.nb_rounds_field.value(), 
                                            player_point=self.view.player_points_field.value())
                    elif launch_response == "LAUNCH_FAIL_NOT_ENOUGH_PLAYER":
                        self.back_to_waiting_room(error_message="Erreur : pas assez de joueurs pour lancer la partie.", 
                                                 username=self.view.username_field.text(),
                                                 room_name=room_name)
                    elif launch_response == "LAUNCH_FAIL_NOT_HOST":
                        self.back_to_waiting_room(error_message="Erreur : seul l'hôte peut lancer la partie.", 
                                                 username=self.view.username_field.text(),
                                                 room_name=room_name)
                    elif launch_response == "LAUNCH_FAIL_NO_LOBBY":
                        self.back_to_waiting_room(error_message="Erreur : la room n'existe pas.", 
                                                 username=self.view.username_field.text(),
                                                 room_name=room_name)
                    elif launch_response == "LAUNCH_FAIL_NO_PLAYER":
                        self.back_to_waiting_room(error_message="Erreur : vous n'êtes pas dans cette room.", 
                                                 username=self.view.username_field.text(),
                                                 room_name=room_name)
                    print("launch")
                    self.current_room = room_name

                elif "-verify" in parts:
                    verify_index = parts.index("-verify") + 1
                    verify_response = parts[verify_index]

                    if verify_response == "SYMBOL_ACK":
                        message = "Bravo ! Symbole correct."
                    elif verify_response == "SYMBOL_FAIL":
                        message = "Dommage ! Symbole incorrect."

                    self.show_game_room(username=self.view.username_field.text(),
                                        room_name=room_name,
                                        nb_round=self.view.nb_rounds_field.value(),
                                        player_point=self.view.player_points_field.value(), 
                                        message=message)

                elif "-chat" in parts:
                    chat_index = parts.index("-chat") + 1
                    chat_message = " ".join(parts[chat_index:])
                    print("message : ",chat_message)
                    if hasattr(self, "current_room") and self.current_room == room_name:
                        if hasattr(self.view, "game_view") and self.view.game_view:
                            self.view.game_view.display_message(chat_message)

    ###
    def send_message(self, message):
        if self.model.connected:
            try:
                self.model.client_socket.send(message.encode("utf-8"))
            except Exception as e:
                raise e
        print("message")

    ###
    def disconnect(self):
        if self.receive_thread:
            self.receive_thread.stop()
            self.model.connected = False

    ###
    def back_to_start_view(self, username, room_name, error_message):
        # Ajouter la logique pour revenir à la vue de démarrage
        pass

    def back_to_waiting_room(self, username, room_name, error_message):
        QMessageBox.critical(
        None,
        "Erreur",
        error_message,
        QMessageBox.Ok
        )
        print("error launch", error_message)

    ###
    def join_waiting_room(self, username, room_name, is_host):
        from view.waiting_room_view import WaitingRoom  
        self.view.waiting_room_view = WaitingRoom(username, room_name, is_host)

        self.view.waiting_room_view.set_controller(self)

        self.view.waiting_room_view.show()
        self.view.hide()

    def leave_waiting_room(self, room_name):
        self.send_message(f"server -room {room_name} -leave")
        self.view.waiting_room_view.hide()
        self.view.show()


    def launch_game(self, room_name, nb_round):
        self.send_message(f"server -room {room_name} -launch {nb_round}")
        print("envoyé 2")


    def show_game_room(self, username, room_name, nb_round, player_point, message=None):
        print("envoyé 3")
        from view.game_view import GameView
        self.view.game_view = GameView(username, room_name, nb_round, player_point)

        self.view.game_view.set_controller(self)

        self.view.waiting_room_view.hide()
        self.view.game_view.show()
