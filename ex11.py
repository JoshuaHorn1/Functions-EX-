def overdue_cost(days_over):
    cost = (days_over * 0.8) + 0.5
    if cost > 30:
        cost = 30
    return cost


# main
days_ = int(input("How many days is your book overdue?: "))
print(f"You owe ${overdue_cost(days_)} for your overdue book.")
