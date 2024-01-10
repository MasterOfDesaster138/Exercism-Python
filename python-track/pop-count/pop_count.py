def egg_count(display_value: int) -> int:
    counter = 0
    binary_num = bin(display_value)[2:]
    
    for num in binary_num:
        if num == '1':
            counter += 1 
    
    return counter 


if __name__ == '__main__':
    egg_count(0)