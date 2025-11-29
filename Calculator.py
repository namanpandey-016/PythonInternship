#Program to calculate (ADD, SUBTRACT, MULTIPLY AND DIVIDE)

print("CALCULATOR")
while True:
    print("""
    1: Add
    2: Subtract
    3: Multiply
    4: Divide
    5: Exit""")
    

    choice = input("Enter your choice: ")
   

    if choice == "1":
        num1 = float (input("Enter Yournfirst Number: "))
        num2 = float (input("Enter Yournfirst Number: "))
        print("The sum is: ", num1 + num2)

    elif choice == "2":
        num1 = float (input("Enter Yournfirst Number: "))
        num2 = float (input("Enter Yournfirst Number: "))
        print("The sum is: ", num1 - num2)       

    elif choice == "3":
        num1 = float (input("Enter Yournfirst Number: "))
        num2 = float (input("Enter Yournfirst Number: "))
        print("The sum is: ", num1 * num2)
        

    elif choice == "4":
        num1 = float (input("Enter Yournfirst Number: "))
        num2 = float (input("Enter Yournfirst Number: "))
        print("The sum is: ", num1 / num2)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
