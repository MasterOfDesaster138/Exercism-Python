""" 
_ green bottles hanging on the wall,
_ green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be _ green bottles hanging on the wall.

"""
# start -> Start value from which one is counted down
# take -> Number of verses output

numbers = {
    0: "no",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight", 
    9: "nine",
    10: "ten", 
}

def recite(start: int, take: int = 1):
    output= []
    counter = 0
    
    for i in range(start, 0, -1):
        output.append(f"{numbers[i].capitalize()} green {bottle_numerus(i)} hanging on the wall,")
        output.append(f"{numbers[i].capitalize()} green {bottle_numerus(i)} hanging on the wall,")
        output.append(f"And if one green bottle should accidentally fall,")
        output.append(f"There'll be {numbers[i - 1]} green {bottle_numerus(i - 1)} hanging on the wall.")
        counter += 1
    
        if counter == take:
            return output
        else:
            output.append("")


def bottle_numerus(quantity: int) -> str:
    return "bottles" if quantity != 1 else "bottle"