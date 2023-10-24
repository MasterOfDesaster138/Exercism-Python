def yacht(dice):
    if dice.count(dice[0]) == 5:
        return 50
    else:
        return 0
    

def ones(dice):
    return dice.count(1) 
    

def twos(dice):
    return dice.count(2) * 2


def threes(dice):
    return dice.count(3) * 3


def fours(dice):
    return dice.count(4) * 4


def fives(dice):
    return dice.count(5) * 5


def sixes(dice):
    return dice.count(6) * 6


def full_house(dice):
    dice = sorted(dice)
    if dice.count(dice[0]) >= 2 and dice.count(dice[-1]) >= 3:
        return sum(dice)
    elif dice.count(dice[0]) >= 3 and dice.count(dice[-1]) >= 2:
        return sum(dice)
    else:
        return 0
    

def four_of_a_kind(dice):
    dice = sorted(dice)
    if dice.count(dice[0]) == 4:
        return dice.count(dice[0]) * 4
    elif dice.count(dice[-1]) >= 4:
        return dice.count(dice[-1]) * 4
    else:
        return 0
    


def little_straight(dice):
    dice_sorted = sorted(dice)
    for i in range(len(dice_sorted)-3):
        if all(dice_sorted[j] - dice_sorted[j-1] == 1 for j in range(i+1, i+4)):
            return 30
    else:
        return 0
    

def big_straight(dice):
    dice_sorted = sorted(dice)

    if all(dice_sorted[i] - dice_sorted[i-1] == 1 for i in range(1, len(dice_sorted))):
        return 30
    else:
        return 0
    

def choice(dice):
    return sum(dice)