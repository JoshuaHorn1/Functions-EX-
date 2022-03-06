def check_status(bmi):
    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


# main
weight = int(input("Enter your weight: "))
print(f"You are {check_status(weight)}, because your weight is {weight}. ")
