TICKET_PRICE = 10
SERVICE_CHARGE = 2 

tickets_remaining = 100

# Calc-Price Funktion 
def calculate_price(ticket_amount):
    return(TICKET_PRICE * ticket_amount + SERVICE_CHARGE)

# Run this code continiously until we are out of tickets
while tickets_remaining > 0:

    # Output how many tickets are remaining using the tickets_remaining variable
    print("{} tickets are remaining".format(tickets_remaining))

    #Gather user's name
    user_name = input("What's your name? ")

    # Prompt user by name and ask how many tickets they would like
    ticket_amount = input("Hello, {} how many tickets do you want? ".format(user_name))
    
    #Handle ValueError
    try:
        ticket_amount = int(ticket_amount)
        if ticket_amount > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err: 
        print("Mayo is not an Instrument! {}".format(err))
    else:
        users_ticket_price = calculate_price(ticket_amount)

        # Output price 
        print("Your total due is {}€".format(users_ticket_price))

        # Prompt user if they want to proceed. Y/N?
        user_proceed = input("Do you want to proceed?\n(Enter Y/N) ")
  
        if user_proceed.upper() == "Y":
            print("SOLD!")
            tickets_remaining -= ticket_amount
            print(tickets_remaining)
        else:
            print("Thanks {}".format(user_name))

# Notify when tickets are out 
print("Out of tickets, sry")

