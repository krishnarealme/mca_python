available_seats={
    "Economy":{"A1": True, "A2": False, "B1": True, "B2": True},
    "Business":{"C1": False, "C2": True, "D1": True, "D2": False}
}

def display_status():
    print("Available Seats: ")
    print("Economy: ")
    print("| Seat | Status |")
    for seat, status in available_seats["Economy"].items():
        print(f"| {seat} | {'Available' if status else 'Booked'} |")
    print("\nBusiness: ")
    print("| Seat | Status |")
    for seat, status in available_seats["Business"].items():
        print(f"| {seat} | {'Available' if status else 'Booked'} |")


def change_status(Class,Seat_No):
    if Class in available_seats and Seat_No in available_seats[Class]:
        if available_seats[Class][Seat_No]:
            available_seats[Class][Seat_No]= False
            return f"Seat {Seat_No} in {Class} class booked successfully."
        else:
            return f"Seat {Seat_No} in {Class} class is already booked."
    else:
        return "Invalid Class or Seat Number."
