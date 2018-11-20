"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
while True:
    sales = float(input("Enter sales: $"))
    if sales <0:
        print("invalid input detected, please restart the function")
        break
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("your bonus is", bonus)






