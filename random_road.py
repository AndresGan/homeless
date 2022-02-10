from dataclasses import field
from turtle import color, distance, fillcolor, title
from typing import final

from bokeh.core.property.numeric import Size
from homeless import StandardHomeless
from field import Field
from coordinate import Coordinate
from bokeh.plotting import figure, output_file, show

def walking(field, homeless, steps, type_homeless):
    begin = [homeless.posicion()]
    x_graph = [0]
    y_graph = [0]
    
    for _ in range (steps-1):
        homeless.walk()
        x, y = homeless.posicion()
        x_graph.append(x)
        x_graph.append(y)
    know_homeless = know_type_homeless(type_homeless)
    graph(x_graph, y_graph, know_homeless, steps)
        
    return homeless.distance_origin()

def simulate_walk(steps, number_of_attemps, type_homeless):
    homeless = []
    distance = []
    
    
    for i in range(number_of_attemps):
        homeless.append(type_homeless(name=f"Rasta cuando {i}"))
        emulate_walk = walking(homeless[i], steps, type_homeless)
        distance.append(round(emulate_walk, 1))
    return distance

def graph(x_graph, y_graph, know, steps):
    paint = figure(title=know, x_axis_label="Pasos", y_axis_label="distancia")
    paint.line(x_graph,y_graph, legend_label =str(steps)+"Pasos")
    final_x = x_graph[-1]
    final_y = y_graph[-1]
    paint.diamond_cross(0, 0, fillcolor="green", line_color="green", size = 18)
    paint.diamond_cross(final_x, final_y, fillcolor="red", line_color="red", size = 18)
    final_stretch_x = [0, final_x]
    final_stretch_y = [0, final_y]
    paint.line(final_stretch_x, final_stretch_y, line_width=2, color="red")
     
    show(paint)
    
def main(walk_distance, number_of_attemps, type_homeless):
    
    for steps in walk_distance:
        distance = simulate_walk(steps, number_of_attemps, type_homeless)
        distance_average = round(sum(distance)/len(distance), 4)
        distance_max = max(distance)
        distance_min = min(distance)
        print(f"{type_homeless.__name__} caminata aleatoria")
        print(f"Media= {distance_average}")    
        print(f"Max = {distance_max}")    
        print(f"Min = {distance_min}")
        
        graph(walk_distance, average_walking_distance)
        
        
        
if __name__ == "__main__":
    walk_distance = [100]
    
    number_of_attemps = 3
    
    main(walk_distance, number_of_attemps, StandardHomeless)   