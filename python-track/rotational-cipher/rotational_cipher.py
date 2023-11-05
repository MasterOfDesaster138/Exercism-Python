def rotate(text: str, key: int) -> str:
    import string
    alphabet: str = string.ascii_lowercase
    cipher: str = ""
    
    for char in text:
        # convert only alphabet characters
        if char.isalpha():
            # separate upper and lower case letters
            if char.isupper():
                # get an index of the current character and the cipher character
                char_position: int = alphabet.find(char.lower())  
                char_index: int = char_position + key
                # check if new index is in range of the alphabet_string
                if char_index > len(alphabet):
                    char_index = char_index - len(alphabet) 
                
                cipher += alphabet[char_index].upper()
                
            else:
                # get an index of the current character and the cipher character
                char_position: int = alphabet.find(char)  
                char_index: int = char_position + key
                # check if new index is in range of the alphabet_string
                if char_index > len(alphabet) - 1:
                    char_index = char_index - len(alphabet) 
                
                cipher += alphabet[char_index]
                
        else:
            cipher += char
            
    return cipher