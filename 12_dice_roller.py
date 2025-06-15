import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}

# 🎲 User Input
number_of_dice = int(input("Enter the number of dice: "))

# 🔄 Roll Dice
dice = [random.randint(1, 6) for _ in range(number_of_dice)]

# 🖼️ Print Dice Side-by-Side
for i in range(5):  # 5 lines per die
    for die in dice:
        print(dice_art[die][i], end=' ')
    print()

# ➕ Total
total = sum(dice)
print(f"\n🎯 Total: {total}")
print(f"🎲 Rolled values: {dice}")
