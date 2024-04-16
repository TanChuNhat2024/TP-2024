import socket

HOST = 'localhost'  # Changez l'hôte si nécessaire
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"Connecté au serveur sur {HOST}:{PORT}")

while True:
    try:
        guess = int(input("Entrez votre devinette (1-100): "))
        client_socket.sendall(str(guess).encode())

        response = client_socket.recv(1024).decode()
        print(response)

        if response.startswith("Félicitations"):
            break
    except ValueError:
        print("Erreur: Veuillez entrer un nombre valide.")

client_socket.close()