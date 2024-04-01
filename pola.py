from pole_trojkata import area_triangle
from pole_prostokata import square_area
from globals import a, b


def area(figure, x=a, y=b):
    match figure:
        case 'kwadrat':
            print(square_area(x, y))
        case 'trojkat':
            print(area_triangle(x, y))
        case 'prostokat':
            print(square_area(x, y))
        case _:
            print("Zla nazwa figury")



