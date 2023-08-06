def square(number):
# raise an error if input is less then 1 or greater then 64
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
# if number equals 1, return grains == 1
    elif number == 1:
        grains_per_square = 1
        return grains_per_square
# get the number of grains of the input field
    else:
        grains_per_square = 2 ** (number - 1)
        return grains_per_square
       


def total():
    grains_per_field = []
    for i in range(1, 64+1):
        current_grains = square(i)
        grains_per_field.append(current_grains)
        
    total_grains = sum(grains_per_field)
    return total_grains

