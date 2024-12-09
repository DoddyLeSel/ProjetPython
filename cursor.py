import pygame

from unit import *
from constante import *

class Cursor:
    
    def __init__(self, x, y, positions, color=RED, color2=BLUE):
        self.x = x
        self.y = y
        self.color = color
        self.color2 = color2
        self.positions = positions
        
    def move_cursor(self,screen,x,y):
        while True :
            for event in pygame.event.get():
            
                if event.type == pygame.KEYDOWN:
                
                    if event.key == pygame.K_LEFT and (self.x-1, self.y) in self.positions and 0 <= self.x-1 < GRID_SIZE and 0 <= self.y < GRID_SIZE:
                        if (self.x, self.y) != (x,y) :
                            self.draw_cursor(screen, self.color2)
                        self.x += -1
                        
                    elif event.key == pygame.K_RIGHT and (self.x+1, self.y) in self.positions and 0 <= self.x+1 < GRID_SIZE and 0 <= self.y < GRID_SIZE:
                        if (self.x, self.y) != (x,y) :
                            self.draw_cursor(screen, self.color2)
                        self.x += 1
                        
                    elif event.key == pygame.K_UP and (self.x, self.y-1) in self.positions and 0 <= self.x < GRID_SIZE and 0 <= self.y-1 < GRID_SIZE:
                        if (self.x, self.y) != (x,y) :
                            self.draw_cursor(screen, self.color2)
                        self.y += -1
                        
                    elif event.key == pygame.K_DOWN and (self.x, self.y+1) in self.positions and 0 <= self.x < GRID_SIZE and 0 <= self.y+1 < GRID_SIZE:
                        if (self.x, self.y) != (x,y) :
                            self.draw_cursor(screen, self.color2)
                        self.y += 1
                        
                    if (self.x, self.y) != (x,y) :
                        self.draw_cursor(screen, self.color)
                    
                    pygame.display.flip()
                
                    if event.key == pygame.K_RETURN:
                        return (self.x, self.y)
                    
    def draw_cursor(self, screen, color):
        pygame.draw.rect(screen, color, (self.x*CELL_SIZE, self.y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, WHITE,(self.x*CELL_SIZE, self.y*CELL_SIZE, CELL_SIZE, CELL_SIZE),1)