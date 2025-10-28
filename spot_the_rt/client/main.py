import socket

def main():
    socket_client_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    adresseIP_serveur = "localhost"
    port_serveur = 55300

    socket_client_TCP.connect((adresseIP_serveur, port_serveur))

    message = "test"
    socket_client_TCP.send(message.encode('utf-8'))

    response = socket_client_TCP.recv(1024)
    print("Réponse server :", response.decode('utf-8'))

    socket_client_TCP.close()


if __name__ == "__main__":
    main()