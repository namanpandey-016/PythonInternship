#A simple program to book movie ticket
mylist = []
def add():
    a = input("Enter Movie you want to add")
    mylist.append(a)
    print("Your Ticket is Booked")

def remov():
    rmv = input("Enter the Movie you want to remove: ")
    if rmv in mylist:
        mylist.remove(rmv)
        print("Your entered Movie ticket is cancelled")
    else :
        print("Your entered Movie is not in list")

def display():
    print("Your Movies are: ")
    print(mylist)

    
print("Book Movie Tickets")
while True:
    print("""
    1: Add Movie
    2: Remove Movie
    3: Display All booked tickets
    4: Exit""")
    

    choice = input("Enter your choice: ")
    
    if choice == "1":
        add()
        
    elif choice == "2":
        remov()
        
    elif choice == "3":
        display()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")


