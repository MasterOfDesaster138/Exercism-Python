def is_valid(isbn):
    # remove hyphens 
    if '-' in isbn:
        isbn = isbn.replace("-", "")
        
    # isbn10-format contains 9 numbers + 1 check character
    # check if isbn consists of 10 characters
    if len(isbn) != 10:
        return False
    
    try:
        # extract all numbers into a list except the check digit
        isbn_numbers = [int(number) for number in isbn[:-1]]
        isbn_check_char = isbn[-1]
    except ValueError:
        return False
    
    # only a number from 1-9 or X is valid as check digit 
    if isbn_check_char.isalpha() and isbn_check_char != "X":
        return False
    
    # calculate the correct check digit for given isbn
    # formula: (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
    isbn_sum: int = 0
    factor: int = 10
    for num in isbn_numbers:
        z = num * factor
        isbn_sum += z
        factor -= 1
    
    # replace X with 10
    if isbn_check_char == "X":
        isbn_sum += 10
    else:
        isbn_sum += int(isbn_check_char)
     
    # isbn is valid if isbn_sum % 11 is 0   
    if isbn_sum % 11 != 0:
        return False
    else: 
        return True