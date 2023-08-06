"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    PREFIX = 'un'
    new_word = PREFIX + word
    return new_word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separatedmake
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    vocab_words = list(vocab_words)


    PREFIX = vocab_words[0]
    new_words = [PREFIX]

    for word in vocab_words[1:]:
        new_word = PREFIX + word
        new_words.append(new_word)


    word_group = ' :: '.join(new_words)
    return word_group


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    cutted_word = word[:-4]
    
    if cutted_word[-1:] == 'i':
        cutted_word_list = list(cutted_word)
        del cutted_word_list[-1]
        cutted_word_list.append('y')
        cutted_word_corrected = "".join(cutted_word_list)
        return cutted_word_corrected

    return cutted_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """

    words_in_sentence = sentence.split()
    adjective = words_in_sentence[index]
    if adjective[-1] == '.':
        verb = adjective[:-1] + 'en'
    else:
        verb = adjective + 'en'
    
    return verb
    
