import socket

def create_server_socket(host,port):
    """
    Crée et initialise le socket serveur en écoute
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Serveur en écoute sur le port {port}...")
    return server_socket