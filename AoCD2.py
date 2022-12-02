f = open("Scripts\AoC2022D2 Input")

f = f.read()

def Part_1(file):
    moves = f.split("\n")

    # a rock, b paper, c scissors
    # x rock, y paper, z scissors
    # 1          2         3
    # 0 points for loss, 3 for draw, 6 for win

    total = 0

    for move in moves:
        move = move.split(" ")
        opp_move = move[0]
        my_move = move[1]

        if my_move == "X":
            total += 1
        elif my_move == "Y":
            total += 2
        elif my_move == "Z":
            total += 3

        if move == ["A", "Z"] or move == ["B", "X"] or move == ["C", "Y"]:
            total += 0
        elif move == ["A", "X"] or move == ["B", "Y"] or move == ["C", "Z"]:
            total += 3
        elif move == ["A", "Y"] or move == ["B", "Z"] or move == ["C", "X"]:
            total += 6

    return total

print(Part_1(f))

def Part_2(file):
    moves = f.split("\n")

    # a rock, b paper, c scissors
    # x lose, y draw, z win
    # 1 rock, 2 paper, 3 scissors
    # 0 points for loss, 3 for draw, 6 for win

    total = 0

    for move in moves:
        move = move.split(" ")
        opp_move = move[0]
        result = move[1]

        if result == "X":
            total += 0
        elif result == "Y":
            total += 3
        elif result == "Z":
            total += 6

        if move == ["A", "Z"] or move == ["B", "Y"] or move == ["C", "X"]:
            total += 2
        elif move == ["A", "X"] or move == ["B", "Z"] or move == ["C", "Y"]:
            total += 3
        elif move == ["A", "Y"] or move == ["B", "X"] or move == ["C", "Z"]:
            total += 1

    return total

print(Part_2(f))