#! /usr/bin/python3.4


#exemple pour un client simple
import socket

#construction du socket :
maConnexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#objet maConnexion qui est un objet socket instancie avec pour argument:
# AF_INET : Famille d'adresse : internet
# SOCK_STREAM : type de socket pour le TCP

#connecter le client :
maConnexion.connect(('localhost',8080))
#on utilise connect pour se connecter au serveur, elle prend aussi un tuple,
# la destination
# le port

#C'est fini a ce niveau on est connectes!

#recuperer un message
message = maConnexion.recv(1024).decode()
print(message)

#traiter l'entree des commandes pour le robot en bouclant : 
maBoucle = True
commande = str()
while maBoucle == True:
	commande = input("Commande pour le vehicule : \n")
	maConnexion.send(commande.encode())
	message = maConnexion.recv(1024).decode()
	print(message)
	if commande == "exit":
		maBoucle = False


