from PyQt5.QtCore import QTimer

class MockClientController:
    """ 
    Ce contrôleur remplace le réseau pour les tests.
    Il simule les réponses du serveur.
    """
    def __init__(self, model):
        self.model = model
        self.message_callback = None

    def connect_to_server(self, ip, port, message_callback, username):
        print(f"[MOCK] Tentative de connexion simulée vers {ip}:{port} pour {username}")
        self.message_callback = message_callback
        
        # On simule une connexion réussie
        self.model.connected = True
        self.model.username = username
        print("[MOCK] Connexion réussie !")

    def send_message(self, message):
        print(f"[MOCK] Envoi du message : {message}")
        
        # --- LOGIQUE DE SIMULATION ---
        
        # Si on envoie "START_GAME", le 'serveur' doit répondre "GAME_START" après un délai
        if message == "START_GAME":
            print("[MOCK] Le serveur a reçu la demande de démarrage...")
            # On utilise QTimer pour simuler un petit délai réseau (1s)
            QTimer.singleShot(1000, lambda: self.simulate_server_response("GAME_START"))

    def disconnect(self):
        print("[MOCK] Déconnexion simulée.")
        self.model.connected = False

    def simulate_server_response(self, message):
        """ Force la réception d'un message """
        if self.message_callback:
            print(f"[MOCK] Réception simulée : {message}")
            self.message_callback(message)