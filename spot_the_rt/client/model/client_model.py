class ClientModel:
    def __init__(self):
        """
        Initialise le modèle client et son état de connexion
        """
        self.client_socket = None
        self.connected = False
