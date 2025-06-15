def kg_to_other(kg):
    print(f"\n{kg} kilograms is:")
    print(f"{kg * 1000:.2f} grams")
    print(f"{kg * 2.20462:.2f} pounds")
    print(f"{kg * 35.274:.2f} ounces")

def g_to_other(g):
    print(f"\n{g} grams is:")
    print(f"{g / 1000:.2f} kilograms")
    print(f"{g * 0.00220462:.2f} pounds")
    print(f"{g * 0.035274:.2f} ounces")

def lb_to_other(lb):
    print(f"\n{lb} pounds is:")
    print(f"{lb * 0.453592:.2f} kilograms")
    print(f"{lb * 453.592:.2f} grams")
    print(f"{lb * 16:.2f} ounces")

def oz_to_other(oz):
    print(f"\n{oz} ounces is:")
    print(f"{oz * 0.0283495:.2f} kilograms")
    print(f"{oz * 28.3495:.2f} grams")
    print(f"{oz / 16:.2f} pounds")

def main():
    while True:
        print("\n⚖️ Weight Converter Menu")
        print("1. Kilograms to other units")
        print("2. Grams to other units")
        print("3. Pounds to other units")
        print("4. Ounces to other units")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            weight = input("Enter weight in kilograms: ")
            if weight.replace('.', '', 1).isdigit():
                kg_to_other(float(weight))
            else:
                print("Invalid number!")

        elif choice == '2':
            weight = input("Enter weight in grams: ")
            if weight.replace('.', '', 1).isdigit():
                g_to_other(float(weight))
            else:
                print("Invalid number!")

        elif choice == '3':
            weight = input("Enter weight in pounds: ")
            if weight.replace('.', '', 1).isdigit():
                lb_to_other(float(weight))
            else:
                print("Invalid number!")

        elif choice == '4':
            weight = input("Enter weight in ounces: ")
            if weight.replace('.', '', 1).isdigit():
                oz_to_other(float(weight))
            else:
                print("Invalid number!")

        elif choice == '5':
            print("Goodbye! Stay healthy 💪")
            break

        else:
            print("Please choose a valid option (1-5).")


if __name__ == '__main__':
    main()
