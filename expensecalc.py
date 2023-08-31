def calculate_total_expenses(expense_list):
    total_expenses = sum(expense_list)
    return total_expenses

def main():
    expenses = []
    while True:
        try:
            expense = float(input("Enter an expense (or 0 to finish): "))
            if expense == 0:
                break
            expenses.append(expense)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    total_expenses = calculate_total_expenses(expenses)
    print("Total expenses:", total_expenses)

if __name__ == "__main__":
    main()

