import random

def roll_dice():

    dice_drawings = {
        1: (
            "┌─────┐",
            "│     │",
            "│  ●  │",
            "│     │",
            "└─────┘"
        ),
        2: (
            "┌─────┐",
            "│ ●   │",
            "│     │",
            "│   ● │",
            "└─────┘"
        ),
        3: (
            "┌─────┐",
            "│ ●   │",
            "│  ●  │",
            "│   ● │",
            "└─────┘"
        ),
        4: (
            "┌─────┐",
            "│ ● ● │",
            "│     │",
            "│ ● ● │",
            "└─────┘"
        ),
        5: (
            "┌─────┐",
            "│ ● ● │",
            "│  ●  │",
            "│ ● ● │",
            "└─────┘"
        ),
        6: (
            "┌─────┐",
            "│ ● ● │",
            "│ ● ● │",
            "│ ● ● │",
            "└─────┘"
        )
    }

    while True:
        roll = input("Roll the dice? (yes/no): ")
        
        while roll.lower() == "yes":
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            
            print("\n".join(dice_drawings[dice1]))
            print("\n".join(dice_drawings[dice2]))
            print(f"You rolled {dice1} and {dice2}. Total: {dice1 + dice2}")

            roll = input("Roll the dice again? (yes/no): ")

        if roll.lower() == "no":
            print("Exiting the dice roller. Thnx!")
            quit()

roll_dice()