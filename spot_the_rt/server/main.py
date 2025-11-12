from model.server_socket import create_server_socket
from controller.server_controller import ServerController
from view.console_view import ConsoleView


def main():
    host = ''
    port = 55305

    view = ConsoleView()
    server_socket = create_server_socket(host, port)
    controller = ServerController(server_socket, view)

    try:
        controller.accept_connections()
    except KeyboardInterrupt:
        print("Serveur arrêté par clavier")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()  