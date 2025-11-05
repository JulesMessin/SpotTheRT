class ConsoleView:
    def display_connection(self, client_address):
        print(f"[+] Client connecté : {client_address}")

    def display_message(self, client_address, message):
        print(f"{client_address} >> {message}")

    def display_disconnection(self, client_address):
        print(f"[-] Client déconnecté : {client_address}")
