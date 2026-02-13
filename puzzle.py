import heapq        #used for priority queue 
from node import Node       

goal = [[1, 2, 3],              #hardcoded goal state and pre made puzzle states
        [4, 5, 6],
        [7, 8, 0]]

pmEasy = [[1, 2, 3],
          [4, 5, 6],
          [0, 7, 8]]

pmMedium = [[1, 3, 6],
            [5, 0, 2],
            [4, 7, 8]]

pmHard = [[1, 5, 2],
          [4, 8, 3],
          [7, 6, 0]]

pmExtraHard = [[1, 4, 2],
               [3, 0, 8],
               [7, 6, 5]]

pmExtraExtraHard = [[7, 5, 8],
                    [1, 3, 6],
                    [2, 4, 0]]

def main(): 
    choice = int(input("Welcome to Leo's 8-Puzzle Solver."                  #user prompt
                   " Type '1' to use a pre-made puzzle," 
                   " or '2' to create your own puzzle." + '\n'))
    

    if choice == 1: 
        while True: 
            difficulty = int(input("Pre-made Puzzle! Select a difficulty (1 to 5).\n"))             #user prompt for pre made puzzles and prints it
            if difficulty == 1: 
                print("Selected 1: Easy!\n")
                puzzle = pmEasy
                print_puzzle(puzzle)
                break
            elif difficulty == 2: 
                print("Selected 2: Medium!\n")
                puzzle = pmMedium
                print_puzzle(puzzle)
                break
            elif difficulty == 3: 
                print("Selected 3: Hard!\n")
                puzzle = pmHard
                print_puzzle(puzzle)
                break
            elif difficulty == 4: 
                print("Selected 4: Extra Hard!\n")
                puzzle = pmExtraHard
                print_puzzle(puzzle)
                break
            elif difficulty == 5: 
                print("Selected 2: Extra Extra Hard!\n")
                puzzle = pmExtraExtraHard
                print_puzzle(puzzle)
                break
            else: 
                print("Please Pick a valid input (0 to 5)")         
    elif choice == 2: 
        print("Create Your Own Puzzle! One By One, row by row, from top to bottom."            #user prompt for creating their own puzzle 
              "Use only digits 1-8 and 0 to represent blank space. No repeats!\n")       
        user_row_one = []
        user_row_two = []
        user_row_three = []

        for i in range(3):                                                      #gets the inputted digit and appends it to new puzzle row by row and prints new puzzle
            user_row_one.append(int(input(f"Row 1, Col {i + 1}: \n")))

        for i in range(3):
            user_row_two.append(int(input(f"Row 1, Col {i + 1}: \n")))

        for i in range(3):
            user_row_three.append(int(input(f"Row 1, Col {i + 1}: \n")))

        puzzle = [user_row_one, 
                  user_row_two, 
                  user_row_three]
        print_puzzle(puzzle)
    
    print("Puzzle loaded. Now Choose the algorithm to run:")                  #user prompt asking for which algorithm to solve the puzzle
    print("1) Uniform Cost Search")
    print("2) A* with the Misplaced Tile heuristic")
    print("3) A* with Manhattan Distance heuristic")

    algochoice = int(input("Enter choice (1-3): \n"))

    while True:                                                               #calls for the general search function with the puzzle and heuristic choice
        if algochoice == 1:
            result = general_search(puzzle, uniform_cost_search)
            break
        elif algochoice == 2: 
            result = general_search(puzzle, misplaced_tiles)
            break
        elif algochoice == 3: 
            result = general_search(puzzle, manhattan_distance)
            break
        else: 
            print ("Please pick a choice (1-3): \n")
    
    if result:                                                                  #concluding the program                                                               
        print("Search Complete! Goodbye\n")
    else: 
        print("No solution found.")
        




def print_puzzle(puzzle):                          #helper function to print puzzle row by row 
    for i in range(0, 3): 
        print(puzzle[i])
    print("\n")


def swap(state, row, col, row2, col2):              #helper function to swap the places of 2 squares (for expand function to move the blank square)
    result = []
    for r in range(3):                              #creates copy of a puzzle's state
        copy_row = []
        for c in range(3):
            copy_row.append(state[r][c])
        result.append(copy_row)

    tmp = result[row][col]                          #swaps the values of the squares and returns result state with the swap change
    result[row][col] = result[row2][col2]
    result[row2][col2] = tmp
    return result

def expand(state):                                                     #helper function to expand a puzzle's state and see the possible outcomes of valid operators to the blank space
    row0 = 0 
    col0 = 0 
    children = []

    for row in range(3):                                               #finds the row and column of the blank space 
        for col in range(3): 
            if state[row][col] == 0: 
                row0 = row
                col0 = col
    
    if col0 > 0:                                                        #move blank space left 
        children.append(swap(state, row0, col0, row0, col0 - 1))

    if col0 < 2:                                                        #move blank space right
        children.append(swap(state, row0, col0, row0, col0 + 1))

    if row0 > 0:                                                        #move blank space up
        children.append(swap(state, row0, col0, row0 - 1, col0))

    if row0 < 2:                                                        #move blank space down 
        children.append(swap(state, row0, col0, row0 + 1, col0 ))
    
    return children
            

def uniform_cost_search(state):                         #heuristic function for uniform cost search (h(n) hardcoded to 0)
    return 0



def misplaced_tiles(state):                                                         #heuristic function for A* that counts the misplaced squares                                                         
    count = 0
    for row in range(3):                                                            #if a space in the current state does not match the space in goal state (excluding the blank), add to count 
        for col in range(3):
            if state[row][col] != goal[row][col] and state[row][col] != 0:
                count += 1
    return count



def manhattan_distance(state):                                      #heuristic function for A* that calculates the manhattan distance of the wrong squares                                    
    distance = 0
    for row in range(3):
        for col in range(3):
            if state[row][col] != goal[row][col]:
                if state[row][col] == 0:                            #exclused the blank space
                    continue
                goal_row = (state[row][col] - 1) // 3               #calculates the correct row and column for the square in the current state
                goal_col = (state[row][col] - 1) % 3
                distance += abs(goal_row - row)                     #adds how far the square is from its goal position 
                distance += abs(goal_col - col)
    return distance





def general_search(puzzle, heuristic):                                          #main general search algorithm for both UCS and A*                                        
    initial = Node(puzzle, 0, heuristic(puzzle), None)                          #initialize the starting node, the priority queue, and the variables for the search
    queue = [] 
    heapq.heappush(queue, initial)                                              #pushes the initial state to queue
    max_queue_size = len(queue)
    nodes_expanded = 0
    beginning = True
    visited = []                                                                #initialize list to track visited puzzle states (to make sure no repeats)
    visited.append(puzzle)

    while True: 
        if not queue:                                                           #if run out of puzzle states to explore
            print('failure')
            return None
        
        if len(queue) > max_queue_size:                                         #updates largest queue
            max_queue_size = len(queue)

        node = heapq.heappop(queue)                                             #removes node with lowest cost (f)

        if beginning:                                                           #if not initial state, prints out the next best puzzle state and the g(n) and h(n) values
            print(f"Starting State: ")
            print_puzzle(node.state)
            beginning = False
        else:
            print(f"The best state to expand with a g(n) = {node.g} and h(n) = {node.h}: ")
            print_puzzle(node.state)

        if node.state == goal:                                                  #if it reaches the goal state, prints the depth, number of nodes expanded, and the max queue size
            print(f"Search depth: {node.g}") 
            print(f"Number of Nodes Expanded: {nodes_expanded}")
            print(f"Max queue size: {max_queue_size}" )
            return node
        
        children = expand(node.state)                                           #generates the possible next states from the current puzzle state     
        nodes_expanded += 1
        for state in children:                                                  #checks if the state has been visited, if not then it marks to as visited
            if state in visited: 
                continue
            visited.append(state)                                                   
            child = Node(state, node.g + 1, heuristic(state), node)             #creates node and updates cost and parent for this next puzzle state and adds it to the queue
            heapq.heappush(queue, child)


if __name__ == "__main__":
    main()