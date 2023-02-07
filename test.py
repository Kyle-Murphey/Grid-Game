import os
import math
from time import sleep

loc = [-1, -1]          #location on grid
validLoc = list()       #record of locations


# getting the grid from file to display
def get_grid(lineToRead):
    tempGrid =[[]]

    #attempt to open the file. If it does not exist, exit the application
    try:
        file = open("grids.txt", "r")
    except(FileNotFoundError):
        print("File containing grid data was not found")
        return -1

    levels = len(file.readlines())  #get how many levels there are to choose from

    #if the entered level/line to read is out of range, attempt to get input again
    if (lineToRead not in range(0, levels)):
        print(f"Invalid level. Please enter a number between 0 and {levels - 1}")
        file.close()
        return -2

    file.seek(0)    #return to the beginning position in the grid file

    #beginning going through the file to find the requested file.
    for pos, line in enumerate(file):
        if pos in [lineToRead]:
            i = 1
            j = 0
            nums = line.strip().replace(",", "")    #remove the commas
            gridLength = math.sqrt(len(nums))       #get the dimension of the grid
            #add the numbers to the correct grid position
            for m in nums:
                tempGrid[j].append(int(m))
                #add a new row to populate
                if (i == gridLength):
                    tempGrid.append([])
                    i = 1
                    j += 1
                    continue
                i += 1
            tempGrid.pop()  #remove the ending empty []
    file.close()
    return tempGrid

# printing the grid
def print_grid(grid):
    i = 0
    for m in grid:
        for n in grid[i]:
            print(n, sep=' ', end=' ')
        print()
        i += 1

# check if grid is complete
def check_grid(grid):
    i = 0
    for m in grid:
        for n in grid[i]:
            if (n == 0):
                return -1
        i += 1
    return 0

# reset the grid to default state and clear the valid location record
def reset_grid(grid, gridStart):
    validLoc.clear()
    grid = [row[:] for row in gridStart]
    return grid

# add a valid location to the location record
def push_loc_list():
    validLoc.append(loc[:])
    print(validLoc)#remove later

# remove a location from the location record
def pop_loc_list():
    validLoc.pop()
    print(validLoc)#remove later

# placing the inputted number into the grid
def place_num(nextNum):
    print(f"{nextNum} PLACED AT {loc}")
    return nextNum

# inputted number cannot be placed at given locationS
def invalid_place(nextNum):
    print(f"{nextNum} CAN NOT BE PLACED AT {loc}")
    return -1



# functions for checking corners, edges, and middle blocks #########
def top_left_corner(nextNum, grid, START):
    if (nextNum == grid[START + 1][START] or
        nextNum == grid[START + 1][START + 1] or
        nextNum == grid[START][START + 1]):
        return invalid_place(nextNum)
    push_loc_list()
    return place_num(nextNum)

def bottom_left_corner(nextNum, grid, START, END):
    if (nextNum == grid[END - 1][START] or
        nextNum == grid[END - 1][START + 1] or
        nextNum == grid[END][START + 1]):
        return invalid_place(nextNum)
    push_loc_list()
    return place_num(nextNum)

def top_right_corner(nextNum, grid, START, END):
    if (nextNum == grid[START + 1][END] or
        nextNum == grid[START + 1][END - 1] or
        nextNum == grid[START][END - 1]):
        return invalid_place(nextNum)
    push_loc_list()
    return place_num(nextNum)

def bottom_right_corner(nextNum, grid, END):
    if (nextNum == grid[END - 1][END] or
        nextNum == grid[END - 1][END - 1] or
        nextNum == grid[END][END - 1]):
        return invalid_place(nextNum)
    push_loc_list()
    return place_num(nextNum)

def left_edge(nextNum, grid, START):
    if (nextNum == grid[loc[0] - 1][START] or
        nextNum == grid[loc[0] + 1][START] or
        nextNum == grid[loc[0]][START + 1] or
        nextNum == grid[loc[0] - 1][START + 1] or
        nextNum == grid[loc[0] + 1][START + 1]):
        return invalid_place(nextNum)
    push_loc_list()
    return place_num(nextNum)

def top_edge(nextNum, grid, START):
    if (nextNum == grid[START][loc[1] - 1] or
        nextNum == grid[START][loc[1] + 1] or
        nextNum == grid[START + 1][loc[1]] or
        nextNum == grid[START + 1][loc[1] - 1] or
        nextNum == grid[START + 1][loc[1] + 1]):
        return invalid_place(nextNum)
    push_loc_list()
    return place_num(nextNum)

def right_edge(nextNum, grid, END):
    if (nextNum == grid[loc[0] - 1][END] or
        nextNum == grid[loc[0] + 1][END] or
        nextNum == grid[loc[0]][END - 1] or
        nextNum == grid[loc[0] - 1][END - 1] or
        nextNum == grid[loc[0] + 1][END - 1]):
        return invalid_place(nextNum)
    push_loc_list()
    return place_num(nextNum)

def bottom_edge(nextNum, grid, END):
    if (nextNum == grid[END][loc[1] - 1] or
        nextNum == grid[END][loc[1] + 1] or
        nextNum == grid[END - 1][loc[1]] or
        nextNum == grid[END - 1][loc[1] - 1] or
        nextNum == grid[END - 1][loc[1] + 1]):
        return invalid_place(nextNum)
    push_loc_list()
    return place_num(nextNum)

def middle_block(nextNum, grid):
    if (nextNum == grid[loc[0] - 1][loc[1]] or
        nextNum == grid[loc[0] + 1][loc[1]] or
        nextNum == grid[loc[0]][loc[1] - 1] or
        nextNum == grid[loc[0]][loc[1] + 1] or
        nextNum == grid[loc[0] - 1][loc[1] - 1] or
        nextNum == grid[loc[0] - 1][loc[1] + 1] or
        nextNum == grid[loc[0] + 1][loc[1] - 1] or
        nextNum == grid[loc[0] + 1][loc[1] + 1]):
        return invalid_place(nextNum)
    push_loc_list()
    return place_num(nextNum)
# end of functions checking corners, edges, and middle blocks #######



# check location logic
def check_input(nextNum, grid, START, END):
    if (grid[loc[0]][loc[1]] != 0):     #number already in location
            return invalid_place(nextNum)

    ## CORNERS ##    
    if (loc[0] == START and loc[1] == START):   #TOP LEFT CORNER
        return top_left_corner(nextNum, grid, START)
        
    if (loc[0] == END and loc[1] == START):     #BOTTOM LEFT CORNER
        return bottom_left_corner(nextNum, grid, START, END)
        
    if (loc[0] == START and loc[1] == END):     #TOP RIGHT CORNER
        return top_right_corner(nextNum, grid, START, END)
        
    if (loc[0] == END and loc[1] == END):   #BOTTOM RIGHT CORNER
        return bottom_right_corner(nextNum, grid, END)

    ## EDGES ##
    if (loc[1] == START):   #LEFT EDGE
        return left_edge(nextNum, grid, START)

    if (loc[0] == START):   #TOP EDGE    
        return top_edge(nextNum, grid, START)

    if (loc[1] == END):     #RIGHT EDGE
        return right_edge(nextNum, grid, END)

    if (loc[0] == END):     #BOTTOM EDGE
        return bottom_edge(nextNum, grid, END)

    ## ANY OTHER BLOCK ##    
    return middle_block(nextNum, grid)



def main():
    global loc
    gridStart = [[]]

    #level select loop
    while True:
        print("Enter level for grid: ", end='')
        lineToRead = input()                    #get the level to play
        #ensure level input is an integer
        try:
            lineToRead = int(lineToRead)
        except(ValueError):
            print("Invalid input: please enter a number.")
            continue
        else:
            gridStart = get_grid(lineToRead)    #beginning state of the grid
            if (gridStart == -1):   return 0    #file not found, close app   
            if (gridStart == -2):   continue    #invalid level input; try again
            break                               #valid input; continue
    
    
    
    grid = [row[:] for row in gridStart]    #grid for manipulation and display 
    nextNum = 0                             #number to be inserted into grid
    
    #main loop
    while (nextNum != 'q'):
        print("(u)ndo, (r)eset, or (q)uit")
        print()
        print_grid(grid)    #display the grid for user
        print("\nnumber to input: ", end='')
        nextNum = input()   #get user number to input

        #undo
        if (nextNum == 'u'):
            endOfList = len(validLoc) - 1
            grid[validLoc[endOfList][0]][validLoc[endOfList][1]] = 0
            os.system('cls')
            pop_loc_list()
            print("UNDO")
            continue
        #reset
        if (nextNum == 'r'):
            grid = reset_grid(grid, gridStart)
            os.system('cls')
            print("RESET")
            continue
        #quit
        if (nextNum =='q'):
            break


        #ensure that the inputted number is an integer
        try:
            nextNum = int(nextNum)  
        except(ValueError):
            print("Invalid input. Please use a number in the range of 1 - 4.")
            continue
        #ensure inputted number is within range
        if (int(nextNum) not in [1, 2, 3, 4]):
            print("Invalid input. Please use a number in the range of 1 - 4.")
            continue

        while True:
            print("row: ", end='')
            loc[0] = input()   #get row
            #ensure input is an integer
            try:
                loc[0] = int(loc[0])
            except(ValueError):
                print(f"Invalid input. Please use a number between 0 and {len(grid)-1}")
                continue
            #ensure input is within range
            if (int(loc[0]) not in range(0, len(grid))):
                print(f"Invalid input. Please use a number between 0 and {len(grid)-1}.")
                continue
            break
        
        while True:
            print("column: ", end='')
            loc[1] = input()   #get column
            #ensure input is an integer
            try:
                loc[1] = int(loc[1])
            except(ValueError):
                print(f"Invalid input. Please use a number between 0 and {len(grid)-1}")
                continue
            #ensure input is within range
            if (int(loc[1]) not in range(0, len(grid))):
                print(f"Invalid input. Please use a number between 0 and {len(grid)-1}.")
                continue
            break

                     
        os.system('cls')        
        output = check_input(nextNum, grid, 0, len(grid) - 1) #begin processing user input
        if (output != -1):  #vaild placement
            grid[loc[0]][loc[1]] = output

        if (check_grid(grid) != -1):    #finished grid
            print_grid(grid)
            print("Grid Complete!")
            break

    print("Good-bye!")
    sleep(2)


if __name__ == "__main__":
    main()
