# Expense Tracker

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = input("Enter expense amount: ")
        category = input("Enter expense category: ")

        file = open("expenses.txt", "a")
        file.write(amount + "," + category + "\n")
        file.close()

        print("Expense added successfully!")

    elif choice == "2":
        try:
            file = open("expenses.txt", "r")
            expenses = file.readlines()
            file.close()

            print("\nAll Expenses:")

            for expense in expenses:
                data = expense.strip().split(",")
                print("Amount:", data[0], "| Category:", data[1])

        except:
            print("No expenses found.")

    elif choice == "3":
        total = 0

        try:
            file = open("expenses.txt", "r")
            expenses = file.readlines()
            file.close()

            for expense in expenses:
                data = expense.strip().split(",")
                total = total + float(data[0])

            print("Total Expenses =", total)

        except:
            print("No expenses found.")

    elif choice == "4":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")