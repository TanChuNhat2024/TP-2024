import socket
import random

HOST = 'localhost'  # Changez l'hôte si nécessaire
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Serveur en attente sur {HOST}:{PORT}")

def handle_client(client_socket):
    number = random.randint(1, 100)
    print(f"Nombre choisi pour le client {client_socket.getpeername()}: {number}")

    while True:
        try:
            guess = int(client_socket.recv(1024).decode())
            print(f"Client {client_socket.getpeername()} a deviné: {guess}")

            if guess == number:
                client_socket.sendall("Félicitations ! Vous avez deviné le nombre.".encode())
            elif guess < number:
                client_socket.sendall(b"Le nombre est plus grand.".encode())
            else:
                client_socket.sendall(b"Le nombre est plus petit.".encode())
        except ValueError:
            client_socket.sendall(b"Erreur: Veuillez entrer un nombre valide.".encode())

while True:
    client_socket, address = server_socket.accept()
    print(f"Client connecté depuis {address}")
    handle_client(client_socket)