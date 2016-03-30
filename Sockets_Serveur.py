#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

#Exemple pour un serveur :)
import socket

#construction du socket
maConnexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#objet maConnexion qui est un objet socket instancie avec pour argument:
# AF_INET : Famille d'adresse : internet
# SOCK_STREAM : type de socket pour le TCP

#connecter le socket :
maConnexion.bind(('',8080))
# bind prend un tuple comme argument, avec
#une IP qui peut varier, donc ""
#un port qui sera toujours le même ici 8080.

#faire écouter le socket :
maConnexion.listen(5)
# max de connexion entrantes en mm temps.
#les connexions etablies ne comptent pas ???

#accepter la connexion  :
connexionClient, infosClient = maConnexion.accept()


#afficher les infos de connexion une fois la connexion acceptee :
print(infosClient) #et non pas maconnexion.infosClient. Ca marche pas

#Evaluer et envoyer un message
connexionClient.send("connexion Acceptee'\n".encode())
try:
	connexionClient.send("connexion acceptee pour %s sur votre port %s".encode() % (infosClient[0],infosClient[1]))
except:
	connexionClient.send("rate!".encode())

maboucle = True
statutLampe = False
while maboucle == True:
	message = connexionClient.recv(1024).decode()
	if message == "exit":
		print("recu : %s" % message)
		connexionClient.send("deconnexion du serveur".encode())
		maConnexion.close()
		maboucle = False
		break
	elif message == "o":
		print("recu : %s" % message)
		connexionClient.send("action: avancer".encode())
	elif message == "k":
		print("recu : %s" % message)
		connexionClient.send("action: tourner gauche".encode())
	elif message == "m":
		print("recu : %s" % message)
		connexionClient.send("action: tourner droite".encode())
	elif message == "l":
		print("recu : %s" % message)
		connexionClient.send("action: reculer".encode())
	elif message == "p" and statutLampe == False:
		print("recu : %s" % message)
		statutLampe = True
		connexionClient.send("action: lampe allumee".encode())
	elif message == "p" and statutLampe == True:
		print("recu : %s" % message)
		statutLampe = False
		connexionClient.send("action: lampe eteinte".encode())
	else:
		print(message)
		connexionClient.send("Commande Inconnue".encode())
		message = ""



