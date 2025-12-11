from bank import Bank


print("===============BANK===============")
print("Commands:")
print("  create_account <name>")
print("  deposit <name> <amount>")
print("  withdraw <name> <amount>")
print("  balance <name>")
print("  delete_account <name>")
print("  exit")


def main():
    bank = Bank()

    while  True:
        command = input(">> ").strip().split()

        if not command:
            continue

        action = command[0]

        if action == "create_account":
            bank.add_client(command[1])

        elif action == "deposit":
            bank.deposit(command[1], float(command[2]))

        elif action == "withdraw":
            bank.withdraw(command[1], float(command[2]))

        elif action == "balance":
            print(bank.get_balance(command[1]))

        elif action == "delete_account":
            bank.remove_client(command[1])

        elif action == "exit":
            print("Exiting banking system.........")
            break

        else:
            print("unknown command, please try again")


if __name__ == "__main__":
    main()