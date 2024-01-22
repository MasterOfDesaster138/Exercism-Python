import string

def abbreviate(words: str) -> str:
    # Replace all hyphens with a whitespace
    processed_words = words.replace('-', ' ')
    # Remove all other punctuation
    translation_table = str.maketrans("", "", string.punctuation)
    # Separate each word into a list
    separated_words = processed_words.translate(translation_table).split()
    # Get the first character of each Word
    acronym = "".join(word[0].upper() for word in separated_words)
        
    return acronym
