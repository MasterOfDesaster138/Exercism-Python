ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
CIPHER = 'zyxwvutsrqponmlkjihgfedcba'

def encode(plain_text: str):
    # initialize the result string
    result = ''
    counter = 0

    # iterate trough each character
    for char in plain_text:
        # check if the character is a letter
        if char.isalpha():
            # the encoding is case insensitive
            char = char.lower()
            # Find the index of the character in the plain alphabet
            index = ALPHABET.find(char)
            # Apply the Atbash substitution
            encrypted_char = CIPHER[index]
            # Append the character to the result
            result += encrypted_char
            counter += 1

            # Add a space every 5 characters
            if counter % 5 == 0:
                result += ' '
                
        # if the character is a number, leave it unchanged
        elif char.isnumeric():
            result += char
            counter += 1
            # Add a space every 5 characters
            if counter % 5 == 0:
                result += ' '

        # exclude whitespace or punctuation in the input string
        else:
            continue
            

    return result.strip() 


def decode(ciphered_text: str):
    # initialize the result string
    result = ''

    # Iterate through each character in the input text
    for char in ciphered_text:
        # Check if the character is a letter
        if char.isalpha():
            # Find the index of the character in the cipher alphabet
            index = CIPHER.find(char)
            
            # Apply the Atbash substitution
            decrypted_char = ALPHABET[index]

            # Append the decrypted character to the result
            result += decrypted_char

        elif char == ' ':
            continue
            
        else: 
        # Include non-alphabetic characters in the result without decryption
            result += char
            
    return result


if __name__ == '__main__':
    encode("dog.")