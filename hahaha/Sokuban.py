map = {
    "size_x": 6,
    "size_y": 6,
}

player = {
    "x": 4,
    "y": 4
}
boxes = [
    {"x": 1, "y": 1},
    {"x": 2, "y": 2},
    {"x": 3, "y": 3},
]
destinations = [
    {"x": 1, "y": 2},
    {"x": 2, "y": 3},
    {"x": 3, "y": 4},
]
obstacles = [
    {"x": 4, "y": 2},
    {"x": 2, "y": 4}
]

walls = [
    {"x": 0, "y": 1},
    {"x": 0, "y": 2},
    {"x": 0, "y": 3},
    {"x": 0, "y": 4},
    {"x": 0, "y": 5},
    {"x": 1, "y": 0},
    {"x": 2, "y": 0},
    {"x": 3, "y": 0},
    {"x": 4, "y": 0},
    {"x": 5, "y": 0},
    {"x": 0, "y": 0},
    {"x": 5, "y": 5},
    {"x": 5, "y": 4},
    {"x": 5, "y": 3},
    {"x": 5, "y": 2},
    {"x": 5, "y": 1},
    {"x": 5, "y": 5},
    {"x": 4, "y": 5},
    {"x": 3, "y": 5},
    {"x": 2, "y": 5},
    {"x": 1, "y": 5},

]

while True:
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            player_is_here = False
            box_is_here = False
            des_is_here = False
            obs_is_here = False
            wall_is_here = False
            for w in walls:
                if w["x"] == x and w["y"] == y:
                    wall_is_here = True
                    break
            for box in boxes:
                if box["x"] == x and box["y"] == y:
                    box_is_here = True
                    break
            for des in destinations:
                if des["x"] == x and des["y"] == y:
                    des_is_here = True
                    break
            for obs in obstacles:
                if obs["x"] == x and obs["y"] == y:
                    obs_is_here = True
                    break
            if x == player["x"] and y == player["y"]:
                player_is_here=True
            if player_is_here:
                print("P", end = " ")
            elif box_is_here:
                print("B", end = " ")
            elif des_is_here:
                print("D", end = " ")
            elif obs_is_here:
                print("O", end = " ")
            elif wall_is_here:
                print("W", end = " ")
            else:
                print("- ", end = "")
        print()
    win = True
    for box in boxes:
        if box not in destinations:
            win = False
    if win:
        print("YOU WIN")
        break
    move = input("Your move or undo: ").upper()
    dx = 0
    dy = 0
    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = - 1
    elif move == "D":
        dx = 1
    else:
        print("Ky tu khong hop le")
    if (0 <= player["x"] +dx <= map["size_x"] - 1) and (0 <= player["y"] + dy <= map ["size_y"] - 1):
        player["x"] += dx
        player["y"] += dy
    for box in boxes:
        if player["x"] == box["x"] and player["y"] == box["y"] and (0 <= box["x"] + dx <= map["size_x"] - 1) and (0 <= box["y"] + dy <= map["size_y"] - 1):
            box["x"] += dx
            box["y"] += dy
    for obs in obstacles:
        if player["x"] == obs["x"] and player["y"] == obs["y"]:
            player["x"] -= dx
            player["y"] -= dy
    for obs in obstacles:
        for box in boxes:
            if box["x"] == obs["x"] and box["y"] == obs["y"]:
                player["x"] -= dx
                player["y"] -= dy
                box["x"] -= dx
                box["y"] -= dy
    for i in range(len(boxes)):
        if (boxes[i]["x"] == boxes[i-1]["x"] and boxes[i]["y"] == boxes[i-1]["y"]) or (boxes[i]["x"] == boxes[i-2]["x"] and boxes[i]["y"] == boxes[i-2]["y"]):
            boxes[i]["x"] -= dx
            boxes[i]["y"] -= dy
    for box in boxes:
        if player["x"] == box["x"] and player["y"] == box["y"]:
            player["x"] -= dx
            player["y"] -= dy
    for wall in walls:
        for box in boxes:
            if box["x"] == wall["x"] and box["y"] == wall["y"]:
                box["x"] -= dx
                box["y"] -= dy
                player["x"] -= dx
                player["y"] -= dy


