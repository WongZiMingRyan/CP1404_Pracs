months_num = int(input("How many months? "))
count = 1
incomes = []

while count <= months_num:
    temp_income = float(input("Enter income for month {}: ".format(count)))
    incomes.append(temp_income)
    count = count + 1


def report_print():
    global count
    print("Income Report")
    print("-------------")
    current_total = 0.00
    count = 1
    while count <= months_num:
        current_total = current_total + incomes[count - 1]
        print("Month {0:>2} - Income: $ {1:>10,.2f} Total: $ {2:>10,.2f}".format(count, incomes[count - 1],
                                                                                 current_total))
        count = count + 1


report_print()
