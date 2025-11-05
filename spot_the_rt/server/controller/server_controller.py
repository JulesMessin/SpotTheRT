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

        for thread in self.clients:
            if thread.client_address == client_address:
                response = message[::-1].encode('utf-8')
                thread.client_socket.send(response)
                break

    def client_disconnected(self, client_address):
        self.clients = [t for t in self.clients if t.client_address != client_address]
        self.view.display_disconnection(client_address)
