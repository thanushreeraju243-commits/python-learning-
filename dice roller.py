import random

#● ┌ ─ ┐ │ └ ┘ 
#            │"
"└─ ─ ─ ─ ─ ─ ─ ─ ┘"
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ), 
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
    }
dice = []
total = 0
num_dice = int(input("How many dice would you like to roll? "))
for _ in range(num_dice):
    dice.append(random.randint(1, 6))
    total += dice[-1]
for die in dice:
    for line in dice_art[die]:
        print(line) 
print(f"Total: {total}")
