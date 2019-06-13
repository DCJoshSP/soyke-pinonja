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



leader_board = {}
val_list = []
final_list = []
game_over = False

while not game_over:
    x = input("Enter a name: ")
    y = input("Enter a score: ")
    leader_board[x] = y
    if input("Do you want to continue y/n? ") == "n":
        game_over = True
    #endif
#endwhile
    
for key in leader_board:
    val_list.append(int(leader_board[key]))
#next
val_list = insertionsort(val_list)

for val in val_list:
    for key in leader_board:
        if leader_board[key] == str(val):
            final_list.append((key, val))
print(final_list)

