import random
def display_hangman(hangman,wrong_guesses):
    for line in hangman[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(answer)

def main():
    hangman = {
        0: (
            " ",
            " ",
            " "
        ),
        1: (
            " o ",
            " ",
            " "
        ),
        2: (
            " o ",
            " |",
            " "
        ),
        3: (
            " o ",
            "/|",
            " "
        ),
        4: (
            " o ",
            "/|\\",
            " "
        ),
        5: (
            " o ",
            "/|\\",
            "/"
        ),
        6: (
            " o ",
            "/|\\",
            "/ \\"
        )
    }
    words = [
        "apple", "banana", "cherry", "date", "elderberry",
        "fig", "grape", "honeydew", "kiwi", "lemon",
        "mango", "nectarine", "orange", "papaya", "quince",
        "raspberry", "strawberry", "tangerine", "ugli", "watermelon"]
    answer=random.choice(words)
    print(answer)
    hint=["_"]*len(answer)
    guessed_letters=[""]
    wrong_guesses=0
    is_running=True

    while is_running:
        print("###############################")
        display_hangman(hangman,wrong_guesses)
        display_hint(hint)
        guess=input("enter your guess(one letter) : ").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid guess")
            continue
        if guess in guessed_letters:
            print(f"{guess}is already guessed")
            continue
        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
        else:
            wrong_guesses += 1
            print("wromg guess....")

        guessed_letters.append(guess)

        if '_' not in hint:
            print("****************************")
            print("You Win!!!!!!!")
            display_hangman(hangman,wrong_guesses)
            print(f"The correct answer is {answer}")
            is_running=False
            print("****************************")

        elif wrong_guesses >=len(hangman)-1:
            print("****************************")
            print("You lose!!!!!")
            display_hangman(hangman,wrong_guesses)
            print(f"The correct answer is {answer}")
            is_running = False
            print("****************************")




if __name__ == '__main__':
    main()
