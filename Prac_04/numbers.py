number_list = []
for x in range(5):
    number_list.append(int(input("Number: ")))
print("The first number is {}".format(number_list[0]))
print("The last number is {}".format(number_list[-1]))
print("The smallest number is {}".format(min(number_list)))
print("The largest number is {}".format(max(number_list)))
print("The average of the numbers is {}".format(sum(number_list)/5))
