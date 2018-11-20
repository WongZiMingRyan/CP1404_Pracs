def main():
    score = get_score()
    if score < 0 or score > 100:
        print("Invalid score")
    elif score < 50:
        print("Bad")
    elif 91 > score > 49:
        print("Passable")
    elif score > 90:
        print("Excellent")


def get_score():
    score = float(input("Enter score: "))
    return score


main()
