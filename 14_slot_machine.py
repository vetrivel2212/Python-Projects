import random
def spin_row(symbols):
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))


def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]== '🍒':
            return bet*2
        if row[0]=='🍉':
            return bet * 3
        if row[0]== '🍋':
            return bet * 5
        if row[0]=='🔔':
            return bet * 8
        if row[0]=='⭐':
            return bet * 10
    else:
        return 0


def main():
    print("welcome to slot machine!!!!!")
    balance=100
    bet=0
    symbols=['🍒','🍉','🍋','🔔','⭐']
    is_playing=True
    choice='y'
    for symbol in symbols:
        print(symbol,end=" ")
    print()
    while is_playing:
        print("#############################")
        if balance <=0 or choice =='n':
            print("Well played......")
            print(f"Your balance : {balance}")
            print("Game Over.....")
            break
        else:
            print(f"Your balance : {balance}")
            bet=input("Place your bet amount : ")

            if not bet.isdigit():
                print("Invalid entry.....")
                continue

            bet=int(bet)
            if bet>balance:
                print("Insufficient funds..... ")
                continue
            if bet<=0:
                print("Bet amount must be greater than zero... ")
                continue

            balance-=bet
            row=spin_row(symbols)
            print("Spinning.....")

            print_row(row)

            payout=get_payout(row,bet)
            balance+=payout

        choice = input("do you want to continiue(y,n) : ").lower()


if __name__=='__main__':
    main()
