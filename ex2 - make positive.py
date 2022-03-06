def positive(num):
    new_val = abs(num)
    return new_val


# main
num_check = int(input("What is the number?: "))
print(f"The absolute value of {num_check} is {positive(num_check)}")
