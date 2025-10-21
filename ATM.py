money = 5000000
name = input("Enter your name: ")

def balance():
    print("Your balance is:", money)

def withdraw(x):
    global money
    money -= x
    print("Current balance is:", money)

def deposit(x):
    global money
    money += x
    print("Current balance is:", money)

def main():
    print("1. Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    return int(input("Enter your choice: "))

while True:
    choice = main()
    match choice:
        case 1:
            balance()
            print()
        case 2:
            x = int(input("Enter amount to withdraw: "))
            withdraw(x)
            print()
        case 3:
            x = int(input("Enter amount to deposit: "))
            deposit(x)
            print()
        case 4:
            print("Thank you for using our ATM service!")
            break
        case _:
            print("Invalid choice. Please try again.")
            print()

