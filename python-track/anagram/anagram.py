"""def find_anagrams(word: str, candidates: list[str]):
    # find case-insensitive anagrams
    word_chars = list(word.lower())
    word_chars.sort()
    anagrams = []
    
    for candidate in candidates:
        candidate_chars = list(candidate.lower())
        candidate_chars.sort()
        
        if word_chars == candidate_chars and candidate.lower() != word.lower():
            anagrams.append(candidate)
            
    return anagrams """
    
    
def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    word_chars = sorted(list(word.lower()))
    return [candidate for candidate in candidates if sorted(list(candidate.lower())) == word_chars and candidate.lower() != word.lower()]



