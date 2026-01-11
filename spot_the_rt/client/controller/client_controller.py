from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
import socket

import os
import random


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
        self.nb_round = None
        self.player_point = None
        self.images = self.load_images()
        self.username = None



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
                        self.show_game_room(
                            username=self.view.username_field.text(),
                            room_name=room_name,
                            nb_round=self.nb_round,
                            player_point=self.player_point
                        )
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

                if "-commoncard" in parts:
                    idx = parts.index("-commoncard") + 1
                    common_card_symbols = parts[idx:]
                    self.common_card_paths = [f"data/images/{sym}.png" for sym in common_card_symbols]
                    self.update_common_card(self.common_card_paths)

                elif "-playercard" in parts:
                    idx = parts.index("-playercard") + 1
                    player_card_symbols = parts[idx:]
                    self.player_card_paths = [f"data/images/{sym}.png" for sym in player_card_symbols]
                    self.update_player_card(self.player_card_paths)

                elif "-chat" in parts:
                    chat_index = parts.index("-chat") + 1
                    chat_message = " ".join(parts[chat_index:])
                    print("message : ",chat_message)
                    if hasattr(self, "current_room") and self.current_room == room_name:
                        if hasattr(self.view, "game_view") and self.view.game_view:
                            self.view.game_view.display_message(chat_message)
                
                elif "-verify" in parts:
                    verify_index = parts.index("-verify") + 1
                    verify_response = parts[verify_index]

                    print("Réponse vérification :", verify_response)

                    if verify_response.startswith("SYMBOL_ACK"):
                        data = verify_response.split("|")
                        player_point = int(data[1])
                        nb_round = int(data[2])
                        cible_cards = data[3].split(",")
                        player_cards = data[4].split(",")

                        self.view.player_point = player_point
                        self.view.nb_round = nb_round
                        self.view.liste_paths_cible = cible_cards
                        self.view.liste_paths_joueur = player_cards
                        self.view.load_new_cards(cible_cards, player_cards)
                        self.view.update_score_round(player_point, nb_round)

                    elif verify_response == "SYMBOL_FAIL":
                        print("Mauvais symbole sélectionné !")


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
        print("je rejoins une room")
        from view.waiting_room_view import WaitingRoom  
        self.view.waiting_room_view = WaitingRoom(username, room_name, is_host)

        self.view.waiting_room_view.set_controller(self)

        self.view.waiting_room_view.show()
        self.view.hide()

    def leave_waiting_room(self, room_name):
        print("je quitte la room")
        self.send_message(f"server -room {room_name} -leave")
        self.view.waiting_room_view.hide()
        self.view.show()


    def launch_game(self, room_name, nb_round):
        self.send_message(f"server -room {room_name} -launch {nb_round}")
        print("envoyé du launch")


    def show_game_room(self, username, room_name, nb_round, player_point, message=None):

        cible_cards, player_cards = self.generate_cards()


        print("la game se lance")
        from view.game_view import GameView
        self.view.game_view = GameView(username, room_name, nb_round, player_point, cible_cards, player_cards)

        self.view.game_view.set_controller(self)

        self.view.waiting_room_view.hide()
        self.view.game_view.show()


    def load_images(self):
        image_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "..", "data", "images")
        image_dir = os.path.normpath(image_dir)

        if not os.path.exists(image_dir):
            raise FileNotFoundError(f"Le dossier d'images n'existe pas : {image_dir}")

        images = [
            os.path.join(image_dir, f)
            for f in os.listdir(image_dir)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp"))
        ]
        return images

    
    def generate_cards(self):
        cible_cards = random.sample(self.images, 8)
        player_cards = random.sample(self.images, 8)
        return cible_cards, player_cards

    import random, os

    import random, os

    def generate_dobble_cards(self, nb_symbols=8):

        if len(self.images) < nb_symbols + 1:
            raise ValueError("Pas assez d'images pour générer les cartes Dobble")

        common_img = random.choice(self.images)

        other_imgs = random.sample([img for img in self.images if img != common_img], nb_symbols*2)

        card1_imgs = [common_img] + other_imgs[:nb_symbols-1]
        card2_imgs = [common_img] + other_imgs[nb_symbols-1:nb_symbols*2-1]

        random.shuffle(card1_imgs)
        random.shuffle(card2_imgs)

        return card1_imgs, card2_imgs



    def verify_symbol(self, symbol_name):
        message = f"server -room {self.room_name} -verify {symbol_name}"
        print(message)
        self.send_message(message)


    def update_common_card(self, card_paths):
        self.common_card_paths = card_paths
        if hasattr(self.view, "game_view") and self.view.game_view:
            self.view.game_view.update_common_card(card_paths)

    def update_player_card(self, card_paths):
        self.player_card_paths = card_paths
        if hasattr(self.view, "game_view") and self.view.game_view:
            self.view.game_view.update_player_card(card_paths)
