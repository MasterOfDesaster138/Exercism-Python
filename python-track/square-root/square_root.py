def square_root(number):
    estimation = 1
    while True:
        if estimation * estimation != number:
            square_number = number / estimation 
            estimation = (estimation + square_number) / 2
        else:
            if estimation * estimation == number:
                return estimation
        
