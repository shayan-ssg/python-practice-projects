while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        name = input("Expense Name: ")
        amount = input("Amount: ")

        with open("expenses.txt", "a") as f:
            f.write(f"{name},{amount}\n")

        print("Expense Added!")

    elif choice == "2":
        try:
            with open("expenses.txt", "r") as f:
                print("\nExpenses:")
                print(f.read())

        except FileNotFoundError:
            print("No expenses found!")

    elif choice == "3":
        total = 0

        try:
            with open("expenses.txt", "r") as f:
                for line in f:
                    name, amount = line.strip().split(",")
                    total += float(amount)

            print(f"Total Expenses: ${total}")

        except FileNotFoundError:
            print("No expenses found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")
