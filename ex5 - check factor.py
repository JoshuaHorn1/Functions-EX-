def check_factor(num1, num2):
    return num1 % num2 == 0


# main
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
if check_factor(first_num, second_num):
    print(f"{second_num} IS a factor of {first_num}")
else:
    print(f"{second_num} IS NOT a factor of {first_num}")
