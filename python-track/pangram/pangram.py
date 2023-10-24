def is_pangram(sentence):
    # initialize a list of the full alphabet
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # initialize a dict with each letter of the alphabet with default value 0
    alphabet_dict = {key: 0 for key in alphabet_list}
    
    # iterate through each character of the sentence
    for char in sentence.split():
        if char.lower() in alphabet_list:
            # count each matching char 
            alphabet_dict[char] += 1
        
    # check if each letter of the alphabet had a match
    for letter in alphabet_dict:
        if alphabet_dict[letter] == 0:
            return False
    # sentence is a pangram if every letter had a match
    return True