"""
The program will take color names as input and output a two digit number, 
even if the input is more than two colors!

The band colors are encoded as follows:

Black: 0
Brown: 1
Red: 2
Orange: 3
Yellow: 4
Green: 5
Blue: 6
Violet: 7
Grey: 8
White: 9

From the example above: brown-green should return 15 
brown-green-violet should return 15 too, ignoring the third color."""

BAND_COLORS = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]

def value(colors: list) -> int:
    result = ''
    for color in colors[:2]:
        result += str(BAND_COLORS.index(color))
    return int(result)