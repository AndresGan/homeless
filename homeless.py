import random
import xxlimited


class HomeLess:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        
    def posicion (self):
        return(self.x, self.y)
    
    def distance_origin(self, other_coordinate):
        return (self.x**2 + self.y**2)**0.5           
class StandardHomeless(HomeLess):
    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        
        return random.choice([(1,0),(-1,0),(0,-1), (0,1)])
    
class ModerateHomeless(HomeLess):
    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        dx, dy = random.choice([(0,2),(0,-2),(2,0),(-2,0)])
        self.x += dx
        self.y += dy
        return[self.x, self.y]
    
class leftHomeless(HomeLess):
    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        dx, dy = random.choice([(0,1),(0,-1),(1,0),(-5,0)])
        self.x += dx
        self.y += dy
        return[self.x, self.y]
    