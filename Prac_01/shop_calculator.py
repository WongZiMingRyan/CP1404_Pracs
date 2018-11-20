all_item_prices = []
numItems = int(input("Please enter number of items"))
for i in range(1, numItems + 1, 1):
    print("please enter price of item ", i)
    item_price = float(input(""))
    if item_price < 0:
        print("Invalid price detected, please restart the function")
        all_item_prices = []
        break
    print("price of item : ", item_price)
    all_item_prices.append(item_price)
total_cost = sum(all_item_prices)
if total_cost >= 100:
    savings = total_cost * 0.1
    total_cost = total_cost * 0.9
    print("You've saved ", savings, "by spending more than $100!")
print("total price for ", numItems, " items is $", total_cost)
