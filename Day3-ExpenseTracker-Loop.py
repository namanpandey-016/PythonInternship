# ExpenseTracker
#This program will track you daily expenses, it will provide an option to add, remove, display and to find the sum of total expenses
 mylist = []
print("Wanna Track you expenses")
while True:
    print("""
    1: Add Expense
    2: Remove
    3: Display
    4: Total
    5: Exit""")
    

    choice = input("Enter your choice: ")
   

    if choice == "1":
        b = int(input("enter your Expense you want to add"))
        mylist.append(b)
        print("Your expense is recorded")

    elif choice == "2":
        num1 = float(input("Enter the value you want to remove: "))
        mylist.remove(num1)
        print("Your entered Expense is removed")        

    elif choice == "3":
        print("Your expenses are: ")
        print(mylist)
        

    elif choice == "4":
        total_sum = sum(mylist)
        print(f"The sum of the Expenses is: {total_sum}")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
