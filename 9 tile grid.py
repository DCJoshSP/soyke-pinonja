import copy

s_grid = [[5,1,7],
          [3,8,6],
          [2,4,0]] #3x3

f_grid = [[1,2,3],
          [4,5,6],
          [7,8,0]]


open_states = {}
closed_states = {}
depth = 0

def calc_heuristic(node):
    h = 0
    for x in range(3):
        for y in range(3):
            if node[x][y] != f_grid[x][y]:
                h = h + 1
    return h


def calc_empty(node):
    for x in range(3):
        try:
            row = node[x].index(0)
            col = x
        except ValueError:
            pass
    return [col, row]


def add_to_list(key, value, dict):
    if key in dict:
        dict[key].append(value)
    else:
        dict[key] = [value]


empty = calc_empty(s_grid)


add_to_list(calc_heuristic(s_grid), s_grid, open_states)
original_node = s_grid
# print(open_states)
while calc_heuristic(original_node) != 0:
    expansion = []
    lowest_score = 999
    for x in open_states:
        if x < lowest_score:
            lowest_score = x
    # print(lowest_score)
    # print(open_states)
    original_node = open_states[lowest_score].pop(0)
    if len(open_states[lowest_score]) == 0:
        open_states.pop(lowest_score)
    print(original_node)
    empty = calc_empty(original_node)
    for x in range(-1, 2, 2):
        current_node = copy.deepcopy(original_node)
        # print(current_node)
        if empty[0] + x != -1:
            try:
                current_node[empty[0]][empty[1]], current_node[empty[0] + x][empty[1]] = current_node[empty[0] + x][
                                                                                             empty[1]], \
                                                                                         current_node[empty[0]][
                                                                                             empty[1]]
                # print(current_node)
                num = calc_heuristic(current_node)
                found = False
                if num in open_states and not found:
                    if current_node in open_states[num]:
                        found = True
                if num in closed_states and not found:
                    if current_node in closed_states[num]:
                        found = True
                if not found:
                    expansion.append(current_node)
            except IndexError:
                pass
    for y in range(-1, 2, 2):
        current_node = copy.deepcopy(original_node)
        if empty[1] + y != -1:
            try:
                current_node[empty[0]][empty[1]], current_node[empty[0]][empty[1] + y] = current_node[empty[0]][
                                                                                             empty[1] + y], \
                                                                                         current_node[empty[0]][
                                                                                             empty[1]]
                # print(current_node)
                num = calc_heuristic(current_node)
                found = False
                if num in open_states and not found:
                    if current_node in open_states[num]:
                        found = True
                if num in closed_states and not found:
                    if current_node in closed_states[num]:
                        found = True
                if not found:
                    expansion.append(current_node)
            except IndexError:
                pass
    # if len(expansion) == 0:
    #     depth -= 1
    # else:
    #     depth += 1
    # print(expansion)
    for node in expansion:
        score = calc_heuristic(node) #+ depth
        add_to_list(score , node, open_states)
    add_to_list(calc_heuristic(original_node), original_node, closed_states)
    # print(closed_states)
    # print(depth)
print(original_node) # depth
