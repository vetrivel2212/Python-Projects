import time

def countdown_timer(seconds):
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        timer = f"{mins:02d}:{secs:02d}"
        print(f"⏳ Time Left: {timer}", end="\r")  # overwrite same line
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Time's up!")

def main():
    try:
        total_seconds = int(input("Enter time in seconds: "))
        if total_seconds <= 0:
            print("❌ Time must be greater than zero.")
        else:
            countdown_timer(total_seconds)
    except ValueError:
        print("❌ Invalid input. Enter a number.")

if __name__ == '__main__':
    main()
