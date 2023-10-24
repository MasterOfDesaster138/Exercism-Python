def is_paired(input_string: str) -> bool:
    # prepare a dict for matching the correct bracket types
    bracket_types = {"(": ")", "[": "]", "{": "}"}
    # initialize a list to cache opening brackets
    opening_brackets = []
    # iterate through each character of the input string
    for char in input_string:
        # check if the current character matches any opening bracket type
        if char in bracket_types.keys():
            # cache opening bracket
            opening_brackets.append(char)
        # check if the current character is a closing character
        elif char in bracket_types.values():
            # check if the closing bracket matches the correct bracket type 
            if not opening_brackets or bracket_types[opening_brackets.pop()] != char:
                return False
     
    # check if there are any opening brackets left in our list       
    return len(opening_brackets) == 0
