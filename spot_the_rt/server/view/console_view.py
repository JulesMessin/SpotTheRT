class ConsoleView:
    def display_connection(self, client_address, client_username):
        print(f"[+] Client connecté : {client_username} ({client_address})")

    def display_message(self, client_address, client_username, message):
        print(f"{client_username} >> {message}")

    def display_disconnection(self, client_address, client_username):
        print(f"[-] Client déconnecté : {client_address} alias {client_username}")
