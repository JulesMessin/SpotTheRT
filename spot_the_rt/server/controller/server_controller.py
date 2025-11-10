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

        if message == "all":
            for thread in self.clients:
                new_message = "message envoyé a tous les clients"
                new_message = new_message.encode('utf-8')
                thread.client_socket.send(new_message)
        else :
            for thread in self.clients:
                if thread.client_address == client_address:
                    new_message = "void"
                    if message == "clement":
                        new_message = "celine"

                    if message == "nolann":
                        new_message = "skincare"

                    if message == "bastien":
                        new_message = "bk"

                    if message == "jules":
                        new_message = "seigneur de moulède alias le grand seigneur"

                    new_message = new_message.encode('utf-8')
                    thread.client_socket.send(new_message)
                    break
        


    def client_disconnected(self, client_address):
        self.clients = [t for t in self.clients if t.client_address != client_address]
        self.view.display_disconnection(client_address)
