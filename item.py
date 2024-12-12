import pygame
import random



from unit import*
from constante import *
from abc import ABC, abstractmethod


class Item(Unit):
    
    def __init__(self, nb_items):
        
        
        #Hérite de la classe Unit
        self.nb_items = nb_items
        self.positions = set()
        
    
    def generer(self):    
        while len(self.positions) < self.nb_items:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            
            self.positions.add((x, y))


    def draw_item(self, screen):
        
        for  x, y in self.positions:
            # Affiche une image ou un rectangle pour représenter le piège
            image = pygame.image.load("img/RodOfAges.JPG").convert_alpha()
            image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
            screen.blit(image, (x * CELL_SIZE,y * CELL_SIZE))
    
    def is_collected (self,x,y):
        
        if (x,y) in self.positions : #verifier si le perso est sur la case de l'objet
            self.has_item = True #le perso possède un objet 
            self.positions.discard((x,y)) #supprimer les coord de l objet du set
            
        