import random


class HomeLess:
    def __init__(self, name):
        self.name = name
        
        
class StandardHomeless(HomeLess):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def walk(self):
        return random.choice([(1,0),(-1,0),(0,-1)])
    