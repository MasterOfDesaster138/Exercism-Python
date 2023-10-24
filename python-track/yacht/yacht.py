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
    if len(set(dice)) != 2:
        return 0
    if dice.count(dice[0]) == 3 or dice.count(dice[0]) == 2:
        return sum(dice)
    return 0
    

def four_of_a_kind(dice):
    for i in range(1, 7):
        if dice.count(i) >= 4:
            return i * 4
    return 0
    


def little_straight(dice):
    dice_set = set(dice)
    if len(dice_set) >= 5 and dice_set.issubset({1, 2, 3, 4, 5}):
        return 30
    else:
        return 0


def big_straight(dice):
    dice_sorted = sorted(dice)

    if dice_sorted == [2, 3, 4, 5, 6]:
        return 30
    else:
        return 0
    

def choice(dice):
    return sum(dice)


# Score categories.
# Change the values as you see fit.
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


categories = {
    YACHT: yacht,
    ONES: ones,
    TWOS: twos,
    THREES: threes,
    FOURS: fours,
    FIVES: fives,
    SIXES: sixes,
    FULL_HOUSE: full_house,
    FOUR_OF_A_KIND: four_of_a_kind,
    LITTLE_STRAIGHT: little_straight,
    BIG_STRAIGHT: big_straight,
    CHOICE: choice
}


def score(dice, category):
    points = categories[category](dice)
    category = points
    return category
