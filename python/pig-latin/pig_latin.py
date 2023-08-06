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

def translate(text):
# convert string to list of characters for proper manipulation
    characters = list(text)

# implement rule 1
    if text[0] in ('a', 'e', 'i', 'o', 'u') or text[0:1] in ('xr', 'yt'):
        translation = text + 'ay'

    else: 
# import rule 3
        if text[1:2] == 'qu':
            prefix = 
            suffix = prefix
            
# implement rule 2            
        constant = characters.pop(0)
        suffix = str(constant) + 'ay'
        translation = constant.extend(suffix)
        return str(translation)

