print("""Electricity bill estimator
""")
price_per_kwh = float(input("Enter cents per kWh: "))
daily_use_kwh = float(input("Enter daily use in kWh: "))
num_days_bill = float(input("Enter number of billing days: "))
print("")
estimated_bill = 0.01 * price_per_kwh * daily_use_kwh * num_days_bill
print("Estimated bill: {:.2f}".format(estimated_bill))