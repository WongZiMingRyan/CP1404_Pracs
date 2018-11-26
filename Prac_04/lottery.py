import random
quick_pick = int(input("How many quick-picks? "))
for x in range(quick_pick):
    picks = []
    picks.append(random.randrange(46))
    for n in range(5):
        check = random.randrange(46)
        while check in picks:
            check = random.randrange(46)
        picks.append(check)
    picks.sort()
    print("{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}".format(picks[0], picks[1], picks[2], picks[3], picks[4], picks[5]))
