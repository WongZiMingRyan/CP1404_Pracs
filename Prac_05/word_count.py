word_list = input("Enter your text: ").split()
word_dict = {}
for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
for key in sorted(word_dict, key=str.lower):
    print(key, ":", word_dict[key])
