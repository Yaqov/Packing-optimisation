import numpy as np
import math
from Visualisation import Visualisation
from sympy import symbols, Eq, solve
from Elipse import Elipse

# Function takes in 2 ellipses and returns the number of common points between them 
def count_common_points(ellipse1:Elipse, ellipse2:Elipse):
    x, y = symbols('x y')
   
    # General equation for ellipses
    eq1 = Eq(((((x-ellipse1.get_x())*math.cos(ellipse1.get_alpha()) - (y-ellipse1.get_y())*math.sin(ellipse1.get_alpha()))**2)/(ellipse1.get_a()**2)) + ((((x-ellipse1.get_x())*math.sin(ellipse1.get_alpha()) + (y-ellipse1.get_y())*math.cos(ellipse1.get_alpha()))**2)/(ellipse1.get_b()**2)) , 1)
    eq2 = Eq(((((x-ellipse2.get_x())*math.cos(ellipse2.get_alpha()) - (y-ellipse2.get_y())*math.sin(ellipse2.get_alpha()))**2)/(ellipse2.get_a()**2)) + ((((x-ellipse2.get_x())*math.sin(ellipse2.get_alpha()) + (y-ellipse2.get_y())*math.cos(ellipse2.get_alpha()))**2)/(ellipse2.get_b()**2)) , 1)

    # Solve the system of equations
    solutions = solve((eq1, eq2), (x, y))

    # Count the number of real solutions
    common_points = sum(1 for sol in solutions if sol[0].is_real and sol[1].is_real)

    return common_points

def main():    
    plot = Visualisation()
    ellipse1 = Elipse(0,0,2,1,0)
    ellipse2 = Elipse(0,0,1,1.5,45)
    ellipse3 = Elipse(2,2,1,1.5,45)
    common_points = count_common_points(ellipse1, ellipse2)

    plot.add_elipse(ellipse1)
    plot.add_elipse(ellipse2)
    plot.add_elipse(ellipse3)
    plot.plot()

    print(common_points) 

if __name__ == "__main__":
    main()