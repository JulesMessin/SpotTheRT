from model.client_thread import ClientThread

class ServerController:
    def __init__(self, server_socket, view):
        self.server_socket = server_socket
        self.view = view
        self.clients = []

    def accept_connections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            thread = ClientThread(client_socket, client_address, self)
            self.clients.append(thread)
            thread.start()
            self.view.display_connection(client_address)

    def handle_message(self, client_address, message):
        self.view.display_message(client_address, message)
        new_message = ""
        # commande
        if message.startswith("void"):
            parts = message.split()
            if len(parts) == 0:
                return

            sender = parts[0]

                # --- Commande -all ---
            if "-setbackground" in parts:
                try:
                    color_index = parts.index("-setbackground") + 1
                    color = parts[color_index]
                    new_message = f"setbackground {color}"
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

        # message
        else:
            new_message = "Voici ton message :"
            for thread in self.clients:
                if thread.client_address == client_address:
                    new_message = new_message.encode('utf-8')
                    thread.client_socket.send(new_message)
                    break

        self.view.display_message(client_address, new_message)


    def client_disconnected(self, client_address):
        self.clients = [t for t in self.clients if t.client_address != client_address]
        self.view.display_disconnection(client_address)
