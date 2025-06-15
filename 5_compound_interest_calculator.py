def calculate_compound_interest(principal, rate, time, n):
    # Convert rate to decimal
    r = rate / 100
    amount = principal * (1 + r / n) ** (n * time)
    compound_interest = amount - principal
    return amount, compound_interest

def main():
    print("💰 Compound Interest Calculator 💰")
    
    try:
        principal = float(input("Enter the principal amount (₹): "))
        rate = float(input("Enter the annual interest rate (%): "))
        time = float(input("Enter the time (in years): "))
        n = int(input("Enter number of times interest applied per year: "))

        amount, ci = calculate_compound_interest(principal, rate, time, n)

        print("\n📊 Results:")
        print(f"Final Amount (A): ₹{amount:.2f}")
        print(f"Compound Interest Earned: ₹{ci:.2f}")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values only.")

if __name__ == '__main__':
    main()
