import math
# Ask the user which calculation they want to do
choice_of = input("Choose either 'investment' or 'bond' from the menu below: \n \
Investment -to calculate the amount of interest you'll earn on investment \n \
Bond - to calculate the amount you'll have to pay on home loan: ")

# If they choose investment then calculate the total they'll get including interest
if choice_of.lower() == "investment":
    amount_deposited = float(input("Enter the amount to deposit: "))
    Interest_rate = float(input("Enter the interest rate: "))
    num_of_years = float(input("Enter the number of years to invest: "))
    type_of_interest = input("Would you like simple or compound interest?: ")
    Interest_rate_ = Interest_rate / 100
    total1 = (amount_deposited) * (1 + Interest_rate_ * num_of_years)
    total2 = (amount_deposited) * math.pow(1 + (Interest_rate_), (num_of_years))
    if type_of_interest.lower() == "simple":
        print(f"The amount you will get after {num_of_years} years at the interest rate of {Interest_rate}% is R{total1}")
    else:
        print(f"The amount you will get after {num_of_years} years at the interest rate of {Interest_rate}% is R{total2}")

# If they choose bond then calculate the amount to pay monthly
elif choice_of.lower() == "bond":
    value_of_house = float(input("Enter the value of the house: "))
    interest_rate = (float(input("Enter the interest rate: "))) / 100
    interest_rate = interest_rate / 12
    mnths_to_repay = float(input("Enter the no of months you plan tom repay: "))
    payment = (interest_rate * value_of_house) / (1 - ((1 + interest_rate)**(-mnths_to_repay)))
    monthly_payment = format(round(payment, 2), ".2f")
    print(f"You will have to pay R{monthly_payment} every month")
else:
    print("Invalid choise")
