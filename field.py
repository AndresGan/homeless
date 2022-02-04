class Field:
    def __init__(self):
        self.homeless_coordinates = {}
    
    def add_homeless(self, homeless, coordinates):
        self.homeless_coordinates[homeless] = coordinates
        
    def move_homeless(self, homeless):
        delta_x, delta_y = homeless.walk()
        
        #path_x.append(path_x[-1]+ delta_X)
        #path_y.append(path_y[-1]+ delta_h)
        
        current_coordinate = self.homeless_coordinates[homeless]
        new_coordinate = current_coordinate.move(delta_x, delta_y)
        self.homeless_coordinates[homeless]
        
    def get_coordinate(self, homeless):
        return self.homeless_coordinates[homeless]