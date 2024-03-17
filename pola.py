from pole_trojkata import area_triangle
from pole_prostokata import square_area
from globals import a, b


def area(figure, a=a, b=b):
    match figure:
        case 'kwadrat':
            print(square_area(a, b))
        case 'trojkat':
            print(area_triangle(a, b))
        case 'prostokat':
            print(square_area(a, b))
        case _:
            print("Zla nazwa figury")


area('trojkat', 5, 10)
