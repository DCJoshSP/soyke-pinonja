import json
import os

def insertionsort(alist):
    n = len(alist)
    for index in range(1, n):
        currentval = alist[index]
        pos = index
        while pos > 0 and alist[pos - 1] > currentval:
            alist[pos] = alist[pos - 1]
            pos = pos - 1
        #endwhile
        alist[pos] = currentval
    #next index
    return alist
#endfunction

def update(leader_board):
    game_over = False
    while not game_over:
        x = input("Enter a name: ")
        y = input("Enter a score: ")
        leader_board[x] = y
        if input("Press ENTER to continute or X to end") != "":
            game_over = True
    #endif
    return leader_board
#endwhile

def convert_to_tuple(leader_board):
    val_list = []
    leader_board2 = []
    for key in leader_board:
        val_list.append(int(leader_board[key]))
    #next
    val_list = insertionsort(val_list)
    for val in val_list:
        for key in leader_board:
            if leader_board[key] == str(val):
                leader_board2.append((key, val))
    return leader_board2



with open("leaderboard.json", "r") as my_file:
    data = my_file.read()
    if data != "":
        leader_board = json.loads(data)
        print("Current leaders:", convert_to_tuple(leader_board))
    else:
        leader_board = {}

leader_board = update(leader_board)


with open("leaderboard.json", "w") as my_file:
    my_file.write(json.dumps(leader_board))




