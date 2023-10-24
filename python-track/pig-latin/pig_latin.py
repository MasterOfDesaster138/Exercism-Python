"""
Regel 1: Wenn ein Wort mit einem Vokal beginnt, fügen Sie am Ende des Wortes ein "ay" hinzu. 
Bitte beachten Sie, dass "xr" und "yt" am Anfang eines Wortes Vokallaute ergeben 
(z. B. "xray" -> "xrayay", "yttria" -> "yttriaay").

Regel 2: Wenn ein Wort mit einem Konsonanten beginnt, verschiebe ihn an das Wortende
und füge ein "ay" an das Wortende an. Konsonanten können aus mehreren Konsonanten bestehen,
auch als Konsonantencluster bezeichnet (z. B. "Stuhl" -> "airchay").

Regel 3: Beginnt ein Wort mit einem Konsonanten, auf den ein "qu" folgt, 
so wird dieser an das Ende des Wortes gestellt 
und ein "ay" angehängt (z. B. "square" -> "aresquay").

Regel 4: Wenn ein Wort ein "y" nach einem Konsonantencluster oder 
als zweiten Buchstaben in einem Wort mit zwei Buchstaben enthält,
bildet es einen Vokallaut (z. B. "rhythm" -> "ythmrhay", "my" -> "ymay").
""" 
# Sets based on the constraints
VOWELS = {"a", "e", "i", "o", "u"}
VOWELS_Y = {"a", "e", "i", "o", "u", "y"}
SPECIALS = {"xr", "yt"}


def translate(text):
    # placeholder for the translation
    piggyfied = []

    # separate each word from the input and iterate through each word
    for word in text.split():
        # check if word starts with a vowel or another special constraint
        if word[0] in VOWELS or word[0:2] in SPECIALS:
            # append 'ay' if it matches the condition
            piggyfied.append(word + "ay")
            continue

        # start at the second character of the word
        for pos in range(1, len(word)):
            # check for vowel or the character 'y'
            if word[pos] in VOWELS_Y:
                # handle 'qu' as a single character
                pos += 1 if word[pos] == 'u' and word[pos - 1] == "q" else 0
                # append 'ay' after current position 
                piggyfied.append(word[pos:] + word[:pos] + "ay")
                break

    return " ".join(piggyfied)
