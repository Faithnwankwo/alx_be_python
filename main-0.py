import sys
from bank_account import BankAccount

account = BankAccount()

if len(sys.argv) > 1:
    command = sys.argv[1]
    if command.startswith("deposit:"):
        amount = float(command.split(":")[1])
        account.deposit(amount)
    elif command.startswith("withdraw:"):
        amount = float(command.split(":")[1])
        account.withdraw(amount)

account.display_balance()
print("Thank you for using the bank app.")
