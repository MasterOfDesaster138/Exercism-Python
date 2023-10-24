def is_pangram(sentence):
    # Convert the sentence to lowercase for case insensitivity
    sentence = sentence.lower()
    # Initialize a set to store unique characters in the sentence
    unique_chars = set()

    # Iterate through each character in the sentence
    for char in sentence:
        if char.isalpha():
            unique_chars.add(char)

    # Check if the set of unique characters has at least 26 letters
    return len(unique_chars) == 26

