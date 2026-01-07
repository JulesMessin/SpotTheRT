from PyQt5.QtCore import QThread, pyqtSignal
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
        if message.startswith("void"):
            parts = message.split()
            if "-setbackground" in parts:
                try:
                    color_index = parts.index("-setbackground") + 1
                    color = parts[color_index]
                    self.view.response_area.setStyleSheet(f"background-color: {color};")
                except IndexError:
                    self.view.display_message("Erreur : couleur manquante")

        elif message.startswith("client"):
            parts = message.split()
            current_room = None
            if "-room" in parts:
                try:
                    room_index = parts.index("-room") + 1
                    room_name = parts[room_index]
                except IndexError:
                    self.view.display_message("Erreur : nom de la room manquant")
                    return

                if "-host" in parts:
                    self.join_waiting_room(username=self.view.username_field.text(),
                                           room_name=room_name,
                                           is_host=True)
                    print("host")

                elif "-join" in parts:
                    self.join_waiting_room(username=self.view.username_field.text(),
                                           room_name=room_name,
                                           is_host=False)
                    current_room = room_name
                    print("join")

                elif "-launch" in parts:
                    self.show_game_room(username=self.view.username_field.text(),
                                           room_name=room_name)
                    print("launch")

                elif "-chat" in parts:
                    new_message = parts.index("-chat") + 1
                    color = parts[color_index]
                    self.show_game_room(username=self.view.username_field.text(),
                                           room_name=room_name)
                    print("message reçu")
                    self.view.game_view.display_message(new_message)        


    ###
    def send_message(self, message):
        if self.model.connected:
            try:
                self.model.client_socket.send(message.encode("utf-8"))
            except Exception as e:
                raise e

    ###
    def disconnect(self):
        if self.receive_thread:
            self.receive_thread.stop()
            self.model.connected = False

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


    def launch_game(self, room_name):
        self.send_message(f"server -room {room_name} -launch")
        print("envoyé 2")


    def show_game_room(self, username, room_name):
        print("envoyé 3")
        from view.game_view import GameView
        self.view.game_view = GameView(username, room_name)

        self.send_message(f"server -room {room_name} -lauch")

        self.view.game_view.set_controller(self)

        self.view.waiting_room_view.hide()
        self.view.game_view.show()
