def spin_row():
    import random
    symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '💎']
    return [random.choice(symbols) for _ in range(3)]
def display_slot_machine(rows):
    for row in rows:
        print(" | ".join(row))
def get_payout(rows,bet):
    if rows[0][0] == rows[0][1] == rows[0][2]:
        if rows[0][0] == '💎':
            return bet * 10
        elif rows[0][0] == '⭐':
            return bet * 5
        elif rows[0][0] == '🍉':
            return bet * 3
        elif rows[0][0] == '🍊':
            return bet * 2
        elif rows[0][0] == '🍋':
            return bet * 1.5
    return 0
def main():
    balance = 100
    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = int(input("Enter your bet amount: "))
        if bet > balance:
            print("You cannot bet more than your current balance.")
            continue
        rows = [spin_row() for _ in range(3)]
        display_slot_machine(rows)
        payout = get_payout(rows, bet)
        if payout > 0:
            print(f"You won ${payout}!")
            balance += payout
        else:
            print("You lost!")
            balance -= bet
    print("Game over! You have run out of money.")
if __name__ == "__main__":
    main()
       
    
    