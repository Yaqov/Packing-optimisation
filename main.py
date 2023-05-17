import numpy as np
import math
from Visualisation import Visualisation
from sympy import symbols, Eq, solve
from Elipse import Elipse

#Function takes in an Ellipse object and returns the equation of the ellipse
# TODO -> pretvori ovu funkciju u dio klase elipse!
def ellipse_equation(ellipse:Elipse):
    x, y = symbols('x y')
    numerator1 = (((x-ellipse.get_x())*math.cos(ellipse.get_alpha_rad()) - (y-ellipse.get_y())*math.sin(ellipse.get_alpha_rad()))**2)
    denominator1 = (ellipse.get_a()**2)

    numerator2 = (((x-ellipse.get_x())*math.sin(ellipse.get_alpha_rad()) + (y-ellipse.get_y())*math.cos(ellipse.get_alpha_rad()))**2)
    denominator2 = (ellipse.get_b()**2)

    return Eq(numerator1/denominator1 + numerator2/denominator2,1)

# Function takes in 2 ellipses and returns the number of common points between them 
def count_common_points(ellipse1:Elipse, ellipse2:Elipse):
    x, y = symbols('x y')

    # General equation for ellipses
    eq1 = ellipse_equation(ellipse1)
    eq2 = ellipse_equation(ellipse2)

    # Solve the system of equations
    solutions = solve((eq1, eq2), (x, y))

    # Count the number of real solutions
    common_points = sum(1 for sol in solutions if sol[0].is_real and sol[1].is_real)

    return common_points


def main():    
    plot = Visualisation()
    ellipse1 = Elipse(0,0,2,1,0)
    ellipse2 = Elipse(2,2,1,1.5,49)
    common_points = count_common_points(ellipse2, ellipse1)
    print(common_points)

    plot.add_elipse(ellipse1)
    plot.add_elipse(ellipse2)
    plot.plot() 

if __name__ == "__main__":
    main()