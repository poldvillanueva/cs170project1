import heapq
from node import Node

goal = [[1, 2, 3], 
        [4, 5, 6],
        [7, 8, 0]]

pmEasy = [[1, 2, 3],
          [4, 5, 0],
          [7, 8, 6]]

pmMedium = [[1, 0, 2],
            [4, 5, 3],
            [7, 8, 6]]

pmHard = [[1, 5, 2],
          [4, 8, 3],
          [7, 6, 0]]

pmExtraHard = [[7, 5, 8],
               [1, 3, 6],
               [2, 4, 0]]

pmExtraExtraHard = [[1, 4, 2],
                    [3, 0, 8],
                    [7, 6, 5]]

def main(): 
    choice = input("Welcome to Leo's 8-Puzzle Solver." 
                   "Type '1' to use a pre-made puzzle," 
                   "or '2' to create your own puzzle." + '\n')
    

    if choice == 1: 
        while True: 
            difficulty = int(input("Pre-made Puzzle! Select a difficulty (0 to 5)." + '\n'))
            if difficulty == 1: 
                print("Selected 1: Easy!\n")
                puzzle = pmEasy
                break
            elif difficulty == 2: 
                print("Selected 2: Medium!\n")
                puzzle = pmMedium
                break
            elif difficulty == 3: 
                print("Selected 3: Hard!\n")
                puzzle = pmHard
                break
            elif difficulty == 4: 
                print("Selected 4: Extra Hard!\n")
                puzzle = pmExtraHard
                break
            elif difficulty == 5: 
                print("Selected 2: Extra Extra Hard!\n")
                puzzle = pmExtraExtraHard
                break
            else: 
                print("Please Pick a valid input (0 to 5)")
    elif choice == 2: 
        print("Your Own Puzzle! One By One, please enter your digits starting with top row, going down the row. Only do digits 0,9 no repeats" + '\n')
        user_row_one = []
        user_row_two = []
        user_row_three = []

        for i in range(3):
            user_row_one.append(int(input(f"Row 1, Col {i+1}: \n")))

        for i in range(3):
            user_row_two.append(int(input(f"Row 1, Col {i+1}: \n")))

        for i in range(3):
            user_row_three.append(int(input(f"Row 1, Col {i+1}: \n")))

        puzzle = [user_row_one, 
                  user_row_two, 
                  user_row_three]
    for i in range(3): 
        print(puzzle[i] + '\n')
    
    print("Puzzle loaded. Now Choose the algorithm to run:\n")
    print("1) Uniform Cost Search\n")
    print("2) A* with the Misplaced Tile heuristic\n")
    print("3) A* with Manhattan Distance heuristic\n")

    algochoice = int(input("Enter choice (1-3): \n"))

    while True:
        if algochoice == 1:
            result = general_search(puzzle, 0)
            break
        elif algochoice == 2: 
            result = general_search(puzzle, misplaced_tiles)
            break
        elif algochoice == 3: 
            result = general_search(puzzle, manhattan_distance)
            break
        else: 
            print ("Please pick a choice (1-3): \n")



def swap(state, r, c, r2, c2): 
    result = []
    for row in range(3):
        copy_row = []
        for col in range(3):
            copy_row.append(state[row][col])
        result.append(copy_row)

    result[r][c] = result[r2][c2]
    result[r2][c2] = result[r][c]
    return result

def expand(state): 
    row0 = 0 
    col0 = 0 
    children = []

    for row in range(3):
        for col in range(3): 
            if state[row][col] == 0: 
                row0 = row
                col0 = col
    
    if col0 > 0: 
        children.append(swap(state, row0, col0, row0, col0 - 1))

    if col0 < 2: 
        children.append(swap(state, row0, col0, row0, col0 + 1))

    if row0 > 0:
        children.append(swap(state, row0, col0, row0 - 1, col0))

    if row < 2: 
        children.append(swap(state, row0, col0, row0 + 1, col0 ))
    
    return children
            
def misplaced_tiles(state): 
    count = 0
    for row in range(3):
        for col in range(3):
            if state[row][col] != goal[r][c] and state[row][col] != 0:
                count += 1
    return count

def manhattan_distance(state): 
    distance = 0
    for row in range(3):
        for col in range(3):
            if state[row][col] != goal[row][col]:
                if state[row][col] == 0:
                    continue
                goal_row = (state[row][col] - 1) // 3
                goal_col = (state[row][col] - 1) % 3
                distance += abs(goal_row - row)
                distance += abs(goal_col - col)
    return distance





def general_search(puzzle, heuristic):
    initial = Node(puzzle, 0, 0, None)
    queue = [] 
    heapq.heappush(queue, (initial.f, initial))

    if not queue:
        print('failure')
        return None
    
    f, node = heapq.heappop(queue)

    if node.state == goal: 
        return node
    
    children = expand(node.state)

    for state in children:
        child = Node(state, node.g + 1)
