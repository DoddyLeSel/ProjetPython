import pygame

from unit import *
from constante import *

class Cursor:
    
    def __init__(self, x, y, color=RED):
        self.x = x
        self.y = y
        self.color = color
    
    def move_cursor(self,screen):
        while True :
            for event in pygame.event.get():
            
                if event.type == pygame.KEYDOWN:
                
                    if event.key == pygame.K_LEFT:
                        self.x += -1
                    elif event.key == pygame.K_RIGHT:
                        self.x += 1
                    elif event.key == pygame.K_UP:
                        self.y += -1
                    elif event.key == pygame.K_DOWN:
                        self.y += 1

                    pygame.draw.rect(screen, self.color, (self.x*CELL_SIZE, self.y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, WHITE,(self.x*CELL_SIZE, self.y*CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
                    
                    pygame.display.flip()
                
                    if event.key == pygame.K_SPACE:
                        return (self.x, self.y)