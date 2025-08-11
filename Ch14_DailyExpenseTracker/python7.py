print("Welcome to the Daily Expense Tracker!")
print()
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
total = 0.0
expense_list = []
while(1):
    input1 = int(input())
    if input1 == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    elif input1 == 1:
        var1 = float(input())
        expense_list.append(var1)
        total += var1
        print("Expense added successfully!")
    elif input1 == 2:
        if len(expense_list) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range (len(expense_list)):
                print(f'{i+1}. {expense_list[i]}')
    elif input1 == 3:
        if len(expense_list) > 0:
            print("Total expense:", total)
            print("Average expense:", total/(len(expense_list)))
        else:
            print("No expenses recorded yet.")
    elif input1 == 4:
        total = 0.0
        expense_list.clear()
        print("All expenses cleared.")
    else:
        print("Invalid choice. Please try again.")
        continue
