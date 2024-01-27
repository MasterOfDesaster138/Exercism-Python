import random

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
        
        
    def ability(self):
        """Determine randomly a ability score with pseudo dice rolling."""
        # Pseudo Dice rolling 4 times 
        dice_rolls = [random.randint(1, 6) for roll in range(4)]
        # Keep only the three largest dice 
        dice_rolls.remove(min(dice_rolls))
        # Return the Sum of the dice rolls
        return sum(dice_rolls)


def modifier(ability_score: int):
    return (ability_score - 10) // 2