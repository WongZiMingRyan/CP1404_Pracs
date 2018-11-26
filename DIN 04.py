name = str(input("Name: "))
vowel_count = 0
for x in name.upper():
    if x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
        vowel_count += 1
print("Out of {0} letters, {1} has {2} vowels".format(len(name), name, vowel_count))