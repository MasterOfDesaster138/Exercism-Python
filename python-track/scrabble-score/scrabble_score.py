def score(word: str) -> int:
    score = 0
    letter_point_mapping = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"], 
        8: ["J", "X"], 
        10: ["Q", "Z"]
    }

    for char in word:
        for key in letter_point_mapping:
            if char.upper() in letter_point_mapping[key]:
                score += key
            
    return score