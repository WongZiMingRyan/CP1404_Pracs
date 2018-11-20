name = str(input("please enter your name"))
file = open("names.txt", 'w')
print("{}".format(name), file=file)
file.close()

file = open("names.txt", 'r')
print("your name is {}".format(file.read()))
file.close()

file = open("numbers.txt", 'r')
numbers = []
for number in file.read().split():
    numbers.append(int(number))
print("the sum is {}".format(sum(numbers)))
file.close()
