#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

#je veux une fenetre pour pouvoir intégrer les images du rover avec : 
# une case à cocher pour la lampe
# quatre boutons pour avancer, reculer, tourner.
# un cadre pour obtenir les informations du rover
# un cadre pour voir les images de la camera.


from tkinter import *

#créer une classe fenêtre qui sera MA fenetre
class maFen(Tkinter.Tk): #maFen herite de l'objet Tk de Tkinter qui représente les fenetres.
	def __init__ (self, parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		pass

roverITF = maFen(Tk)
roverITF.title("Interface Rover")


roverITF.mainloop
