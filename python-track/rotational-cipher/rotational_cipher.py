def rotate(text: str, key: int) -> str:
    import string
    ALPHABET: str = string.ascii_lowercase
    cipher: str = ""
    
    for char in text:
        # convert only alphabet characters
        if char.isalpha():
            # separate upper and lower case letters
            if char.isupper():
                cipher += ALPHABET[(ALPHABET.index(char.lower()) + key) % 26].upper()
                
            else:
                cipher += ALPHABET[(ALPHABET.index(char) + key) % 26]
                
        else:
            cipher += char
            
    return cipher