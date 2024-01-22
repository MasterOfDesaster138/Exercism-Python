def say(number: int) -> str:
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    
    if number == 0:
        return "zero"
    
    # Define words for powers of 10
    scales = ["", "thousand", "million", "billion"]
    chunks = []
    
    for scale in scales:
        # Extract the last three digits
        chunk = number % 1000
        if chunk != 0:
            chunks.append(say_chunk(chunk) + " " + scale)
        number //= 1000
        
    return " ".join(reversed(chunks)).strip()


def say_chunk(number: int):
    # Define words for numbers up to 19
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    # Define words for tens
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if number == 0:
        return ""
    elif number < 20:
        return ones[number]
    elif number < 100:
        return tens[number // 10] + ("-" + ones[number % 10] if number % 10 != 0 else "")
    else:
        return ones[number // 100] + " hundred " + (say_chunk(number % 100) if number % 100 != 0 else "")