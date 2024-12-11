from constante import *
import pygame
import random

class Mure:
    def __init__(self, nb_murs):
        self.nb_murs = nb_murs
        self.positions = set()  # Ensemble pour éviter les doublons

    def generer_murs(self):
        """Génère des positions uniques pour les murs."""
        while len(self.positions) < self.nb_murs:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            self.positions.add((x, y))  # Ajoute la position à l'ensemble

    def dessiner_murs(self, screen):
        """Dessine les murs comme des rectangles gris."""
        for x, y in self.positions:
            pygame.draw.rect(
                screen,
                GREEN,  # Couleur grise
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )
