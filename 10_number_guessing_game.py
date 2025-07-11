//guess the number randomly generated by a system
import random

low = 1
high = 100
answer = random.randint(low, high)
print(f"🎯 Select a number between {low} and {high}!")

is_running = True
guesses = 0

while is_running:
    guess = input("Enter your guess: ")
    guesses += 1

    if guess.isdigit():
        guess = int(guess)

        if guess < low or guess > high:
            print("🚫 Out of bounds!")
        elif guess < answer:
            print("📉 Too low!")
        elif guess > answer:
            print("📈 Too high!")
        else:
            print("✅ Correct!")
            print(f"🎉 The answer is {answer}")
            print(f"🔁 Number of tries: {guesses}")
            is_running = False
    else:
        print("⚠️ Invalid entry. Please enter numbers only.")
