from Flight_Tkt import display_status,change_status

def display_options():
    print("Options: ")
    print("1.Display status")
    print("2.Change status")

def get_inp():
    Class=input("Enter class(Economy/Business): ").capitalize()
    Seat_No=input("Enter Seat Number: ").upper()
    return Class, Seat_No

while True:
    display_options()
    get_choice=int(input("Enter a choice (1 or 2, 3 to exit): "))
    if get_choice==3:
        break
    if get_choice==1:
        display_status()
    elif get_choice==2:
        Class, Seat_No = get_inp()
        result = change_status(Class, Seat_No)
        print(result)
    else:
        print("Invalid choice. Please enter '1' or '2' ")
    
