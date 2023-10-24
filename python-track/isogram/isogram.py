def is_isogram(string):
    # convert string to lowercase
    input_string = string.lower()
    # create a set to cache unique letters
    seen = set()
    
    for char in input_string:
        # only check for alphabet letters
        if char.isalpha():
            # check if char is already in the seen set
            if char in seen:
                # then it is not a isogram
                return False

            # otherwise add the char to the seen set
            seen.add(char)
        
    # If the loop is completed without repetitions, it is an isogram
    return True