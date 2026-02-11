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
            user_row_one[i] = int(input(f"Row 1, Col {i+1}: \n"))

        for i in range(3):
            user_row_two[i] = int(input(f"Row 1, Col {i+1}: \n"))

        for i in range(3):
            user_row_three[i] = int(input(f"Row 1, Col {i+1}: \n"))

        puzzle = [user_row_one, 
                  user_row_two, 
                  user_row_three]
    
    print("Puzzle loaded. Now Choose the algorithm to run:\n")
    print("1) Uniform Cost Search\n")
    print("2) A* with the Misplaced Tile heuristic\n")
    print("3) A* with Manhattan Distance heuristic\n")

    algochoice = int(input("Enter choice (1-3): \n"))

    if algochoice == 1


def uniform_cost_search(puzzle, heuristic): 


def 

    
    
        
    