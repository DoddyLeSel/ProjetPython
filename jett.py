from unit import *

class Jett(Unit):
    
    def __init__(self, x, y, team):
        
        VIE = 10
        DAMAGE = 2
        
        super().__init__(x, y, VIE, DAMAGE, team)