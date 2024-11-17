from unit import *

class Jett(Unit):
    
    VIE = 100
    DAMAGE = 20
    
    def __init__(self, x, y, team):
        super().__init__(x, y, VIE, DAMAGE, team)