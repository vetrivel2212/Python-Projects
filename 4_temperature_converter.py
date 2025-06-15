def celsius_to_other(c):
    print(f"\n🌡️ {c}°C is:")
    print(f"{(c * 9/5) + 32:.2f}°F")
    print(f"{c + 273.15:.2f}K")

def fahrenheit_to_other(f):
    print(f"\n🌡️ {f}°F is:")
    print(f"{(f - 32) * 5/9:.2f}°C")
    print(f"{((f - 32) * 5/9) + 273.15:.2f}K")

def kelvin_to_other(k):
    print(f"\n🌡️ {k}K is:")
    print(f"{k - 273.15:.2f}°C")
    print(f"{(k - 273.15) * 9/5 + 32:.2f}°F")

def main():
    while True:
        print("\n🔥 Temperature Converter 🌡️")
        print("1. Celsius to Fahrenheit & Kelvin")
        print("2. Fahrenheit to Celsius & Kelvin")
        print("3. Kelvin to Celsius & Fahrenheit")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            temp = input("Enter temperature in °C: ")
            if temp.replace('.', '', 1).lstrip('-').isdigit():
                celsius_to_other(float(temp))
            else:
                print("❌ Invalid input!")

        elif choice == '2':
            temp = input("Enter temperature in °F: ")
            if temp.replace('.', '', 1).lstrip('-').isdigit():
                fahrenheit_to_other(float(temp))
            else:
                print("❌ Invalid input!")

        elif choice == '3':
            temp = input("Enter temperature in K: ")
            if temp.replace('.', '', 1).isdigit():
                kelvin_to_other(float(temp))
            else:
                print("❌ Invalid input!")

        elif choice == '4':
            print("Bye! Stay cool or stay warm ☀️❄️")
            break
        else:
            print("Please enter a valid option (1-4).")

if __name__ == '__main__':
    main()
