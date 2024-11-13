def deposit():
    global bal
    amount_d = float(input("Enter amount to deposit: "))
    bal +=amount_d
    return 0

def withdraw():
    global bal
    amount_w = float(input("Enter amount to withdraw: "))
    if bal < amount_w:
        print("........................................................")
        print("insufficient balance")
        print("........................................................")
    else:
        bal -=amount_w
    return 0

def check_bal():
    print("........................................................")
    print(f"Your current balance is: {bal}$")
    print("........................................................")
bal = 0
running = True

if __name__ == "__main__":
    while running:
        print("........................................................")
        print("Welcome to AQTie Online Banking")
        print("........................................................")
        
        print("1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Which operation would you like to perform? ")
        
        if choice == "1":
            check_bal()
        elif choice == "2":
            deposit()
            print("........................................................")
            print(f"New balance: {bal}$")
            print("........................................................")
        elif choice == "3":
            withdraw()
            print("........................................................")
            print(f"New balance: {bal}$")
            print("........................................................")
        elif choice == "4":
            running = False
        else:
            print("Invalid operation")

    print("........................................................")
    print("Thank you for banking with us")
    print("........................................................")