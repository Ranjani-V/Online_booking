= input("Enter the passenger's age :")
    proof_for_identity = input("Enter passenger's proof for identity:")
    return passenger_name,age,proof_for_identity

def total_fare(destination):
    fare = {
         "Chennai to Bangalore": 1500,
         "Chennai to Trivandrum": 1200,
         "Chennai to Hyderabad": 1400
    }
    return fare[destination]
def payment_mode():
    mode_of_payment ={
         1:"UPI",
         2:"Card",
         3: "Pay later",
         4:"Pay with wallet balance"
    }
    return mode_of_payment
    print("available_payment_methods")
    for key, value in mode_of_payment.items():
     print(f"{key}. {value}")
     payment_choice = int(input("Choose your payment mode: "))
    return mode_of_payment.get(payment_choice, "Invalid choice")


def confirm_booking(passenger_name,age,proof_for_identity,destination,fare):
    print("\n Confirmation")
    print(f"Your name is {passenger_name}")
    print(f"Your age is {age}")
    print(f"Your proof for identity is{proof_for_identity}")
    print(f"Your destination is {destination}")
    print(f"Your total fare is {fare}")
    confirm_ticket_booking= input("Yes or No")
    return confirm_ticket_booking == "Yes"

def main():
    print("Welcome to RedBus Travels")
    destination = destination_choices()
    destination = selection_your_destination(destination)
    passenger_name, age, proof_for_identity= passenger_details
    fare=total_fare(destination)

    if confirm_booking(passenger_name, age, proof_for_identity, fare):
      print("\nYour booking is successful, enjoy your journey")
    else:
      print("Booking is cancelled")


main()




























