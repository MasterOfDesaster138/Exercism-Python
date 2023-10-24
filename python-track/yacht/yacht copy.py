"""
The dice game [Yacht][yacht] is from the same family as Poker Dice, Generala and particularly Yahtzee, of which it is a precursor.
In the game, five dice are rolled and the result can be entered in any of twelve categories.
The score of a throw of the dice depends on category chosen.

## Scores in Yacht

| Category | Score | Description | Example |
| -------- | ----- | ----------- | ------- |
| Ones | 1 × number of ones | Any combination | 1 1 1 4 5 scores 3 |
| Twos | 2 × number of twos | Any combination | 2 2 3 4 5 scores 4 |
| Threes | 3 × number of threes | Any combination | 3 3 3 3 3 scores 15 |
| Fours | 4 × number of fours | Any combination | 1 2 3 3 5 scores 0 |
| Fives | 5 × number of fives| Any combination | 5 1 5 2 5 scores 15 |
| Sixes | 6 × number of sixes | Any combination | 2 3 4 5 6 scores 6 |
| Full House | Total of the dice | Three of one number and two of another | 3 3 3 5 5 scores 19 |
| Four of a Kind | Total of the four dice | At least four dice showing the same face | 4 4 4 4 6 scores 16 |
| Little Straight |  30 points | 1-2-3-4-5 | 1 2 3 4 5 scores 30 |
| Big Straight | 30 points | 2-3-4-5-6 | 2 3 4 5 6 scores 30 |
| Choice | Sum of the dice | Any combination | 2 3 3 4 6 scores 18 |
| Yacht | 50 points | All five dice showing the same face | 4 4 4 4 4 scores 50 |

If the dice do not satisfy the requirements of a category, the score is zero.
If, for example, *Four Of A Kind* is entered in the *Yacht* category, zero points are scored.
A *Yacht* scores zero if entered in the *Full House* category.
"""

# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = None
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    # get Category Constants into function scope
    global YACHT, ONES, TWOS, THREES, FOURS, FIVES, SIXES, FULL_HOUSE, FOUR_OF_A_KIND, LITTLE_STRAIGHT, BIG_STRAIGHT, CHOICE

    # check category value and execute matching function to get the score
    if category == 'YACHT':
    # True if all numbers are equal in dice
        if dice.count(dice[0]) == 5:
            score = 50
        else:
            score = 0
        YACHT = score
        return score
    
    elif category == 'ONES':
    # Count of number 1 => score
        score = dice.count(1) 
        ONES = score
        return score
    
    elif category == 'TWOS':
    # Count of number 2 => score
        score = dice.count(2) * 2
        TWOS = score
        return score
    
    elif category == 'THREES':
    # Count of number 3 => score
        score = dice.count(3) * 3
        THREES = score
        return score
    
    elif category == 'FOURS':
    # Count of number 4 => score
        score = dice.count(4) * 4
        FOURS = score
        return score
    
    elif category == 'FIVES':
    # Count of number 5 => score
        score = dice.count(5) * 5
        FIVES = score
        return score
    
    elif category == 'SIXES':
    # Count of number 6 => score
        score = dice.count(6) * 6
        SIXES = score
        return score
    
    elif category == 'FULL_HOUSE':
        dice = sorted(dice)

# True if 3 from one number and 2 from another number
        if dice.count(dice[0]) >= 2 and dice.count(dice[-1]) >= 3:
            score = sum(dice)
        elif dice.count(dice[0]) >= 3 and dice.count(dice[-1]) >= 2:
            score = sum(dice)
        else:
            score = 0

        FULL_HOUSE = score
        return score
    
    elif category == 'FOUR_OF_A_KIND':
        dice = sorted(dice)
# true if 4 from one number in dices
        if dice.count(dice[0]) == 4:
            score = dice.count(dice[0]) * 4
        elif dice.count(dice[-1]) >= 4:
            score = dice.count(dice[-1]) * 4
        else:
            score = 0

        FOUR_OF_A_KIND = score
        return score
    
    elif category == 'LITTLE_STRAIGHT':
        dice_sorted = sorted(dice)
# check if there is a range of 4 numbers in dices 
        for i in range(len(dice_sorted)-3):
            if all(dice_sorted[j] - dice_sorted[j-1] == 1 for j in range(i+1, i+4)):
                score = 30
            else:
                score = 0
        
        LITTLE_STRAIGHT = score
        return score
    
    elif category == 'BIG_STRAIGHT':
        dice_sorted = sorted(dice)
# check if there is a range of 5 numbers in dices 
        if all(dice_sorted[i] - dice_sorted[i-1] == 1 for i in range(1, len(dice_sorted))):
            score = 30
        else:
            score = 0
    
        BIG_STRAIGHT = score
        return score
    
    elif category == 'CHOICE':
# sum all numbers in dice
        score = sum(dice)
        CHOICE = score
        return score
    

    


