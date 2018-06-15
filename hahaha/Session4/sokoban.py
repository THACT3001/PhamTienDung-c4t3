map = {
    "size_x": 5,
    "size_y":5
}

player = {
    "x": 3,
    "y": 2
}

boxes = [
    {
        "x": 1,
        "y": 1
    },
    {
        "x": 2,
        "y": 2

    },
    {
        "x": 3,
        "y": 3
    }
]

destinations = [
    {
        "x": 0,
        "y": 1
    },
    {
        "x": 1,
        "y": 2
    },
    {
        "x": 2,
        "y": 3
    }
]

play = True

while play:
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):

            box_is_here = False
            player_is_here = False
            destination_is_here = False
            for box in boxes:
                if box["x"] == x and box["y"] == y:
                    box_is_here = True
                    break
            for destination in destinations:
                if destination["x"] == x and destination["y"] == y:
                    destination_is_here = True
                    break
            if player["x"] == x and player["y"] == y:
                player_is_here = True
            if destination_is_here:
                print("D", end = " ")
            elif player_is_here:
                print("P", end = " ")
            elif box_is_here:
                print("B", end = " ")
            else:
                print("-", end = " ")
        print()

    move = input("Your move: ").upper()

    dx = 0
    dy = 0

    if move == "W":
        print("Up")
        dy = -1
    elif move == "S":
        print("Down")
        dy = 1
    elif move == "A":
        print("Left")
        dx = -1
    elif move == "D":
        print("Right")
        dx = 1
    else:
        print("Meh")
        break
    if 0 <= player["x"] + dx < map["size_x"] and 0 <= player["y"] + dy < map["size_y"]:
        player["x"] += dx
        player["y"] += dy
    if player["x"] == boxes[1]["x"] and player["y"] == boxes[1]["y"]:
        boxes[1]["x"] = boxes[1]["x"] + dx
        boxes[1]["y"] = boxes[1]["y"] + dy
    if player["x"] == boxes[2]["x"] and player["y"] == boxes[2]["y"]:
        boxes[2]["x"] = boxes[2]["x"] + dx
        boxes[2]["y"] = boxes[2]["y"] + dy
    if player["x"] == boxes[0]["x"] and player["y"] == boxes[0]["y"]:
        boxes[0]["x"] = boxes[0]["x"] + dx
        boxes[0]["y"] = boxes[0]["y"] + dy
    win = True
    for box in boxes:
        if box not in destinations:
            win = False

        elif win:
            print("YOU WIN!!")
            play = False
