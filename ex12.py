def main_routine():
    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    total_sales = 0
    tickets_sold = 0

    ticket_wanted = input("Do you want to sell a ticket? (Y/N):").upper()
    while ticket_wanted != "N":
        ticket = sell_ticket()

        num_tickets = int(input("How many of these tickets do you want: "))
        confim = input(f"Confirm purchase of {num_tickets} type {ticket} "
                        f"ticket/s? (Y/N: ").upper()
        if confirm == "Y"
            price = num_tickets * float(get_price(ticket))
            total_sales += price
            tickets_sold += num_tickets
            if ticket == "A":
                adult_tickets += 1
            elif ticket == "S":
                student_tickets += 1
            elif ticket == "C":
                child_tickets += 1
            else:
                gift_tickets += 1

            ticket_wanted = input("\nDo you want to sell"
                                  "another ticket? Y?N").upper()

        print("==========================================================")
        print
