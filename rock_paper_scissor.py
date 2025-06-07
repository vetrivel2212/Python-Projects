import random

options = ["rock", "paper", "scissor"]
computer_score = 0
player_score = 0

is_running = True

while is_running:
    computer = random.choice(options)
    player = input("Enter your choice (rock, paper, scissor): ").lower()

    if player not in options:
        print("❌ Invalid choice! Try again.")
        continue

    print(f"🧠 Opponent chose: {computer}")

    if computer == player:
        print("🤝 It's a tie!")
    elif (computer == "rock" and player == "paper") or \
         (computer == "paper" and player == "scissor") or \
         (computer == "scissor" and player == "rock"):
        player_score += 1
        print("✅ You won this round!")
    else:
        computer_score += 1
        print("💢 Opponent won this round.")

    choice = input("Do you want to continue? (y/n): ").lower()
    if choice == 'n':
        is_running = False

print("\n***********************************************")
print("🏁 Game Over! Final Scores:")
print(f"🧍‍♂️ Your Score     : {player_score}")
print(f"🤖 Opponent Score : {computer_score}")

if player_score > computer_score:
    print("🏆 You are the champion!")
elif player_score < computer_score:
    print("😓 Opponent wins this time.")
else:
    print("⚖️ It's a draw!")
print("***********************************************")

