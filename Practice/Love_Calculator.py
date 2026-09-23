def calculate_love_score(name1, name2):
    true = 0
    love = 0

    for letter in name1.upper() + name2.upper():
        if letter == "T":
            true += 1
        elif letter == "R":
            true += 1
        elif letter == "U":
            true += 1
        elif letter == "E":
            true += 1

    for letter in name1.upper() + name2.upper():
        if letter == "L":
            love += 1
        elif letter == "O":
            love += 1
        elif letter == "V":
            love += 1
        elif letter == "E":
            love += 1

    print(f"{true}{love}")


calculate_love_score("rahul", "sita")
