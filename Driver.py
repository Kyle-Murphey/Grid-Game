import os
import math
from time import sleep
from Game import Game


# constant for invalid input
INVALID = -1


# getting the grid from file to display
def getGrid(lineToRead):
    tempGrid = [[]]

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


######### functions for checking corners, edges, and middle blocks #########
def top_left_corner(game, START):
    if (game.getNextNum() == game.getGrid()[START + 1][START] or
        game.getNextNum() == game.getGrid()[START + 1][START + 1] or
        game.getNextNum() == game.getGrid()[START][START + 1]):
        return game.placeNextNum(INVALID)
    game.pushValidLoc()
    return game.placeNextNum(game.getNextNum())

def bottom_left_corner(game, START, END):
    if (game.getNextNum() == game.getGrid()[END - 1][START] or
        game.getNextNum() == game.getGrid()[END - 1][START + 1] or
        game.getNextNum() == game.getGrid()[END][START + 1]):
        return game.placeNextNum(INVALID)
    game.pushValidLoc()
    return game.placeNextNum(game.getNextNum())

def top_right_corner(game, START, END):
    if (game.getNextNum() == game.getGrid()[START + 1][END] or
        game.getNextNum() == game.getGrid()[START + 1][END - 1] or
        game.getNextNum() == game.getGrid()[START][END - 1]):
        return game.placeNextNum(INVALID)
    game.pushValidLoc()
    return game.placeNextNum(game.getNextNum())

def bottom_right_corner(game, END):
    if (game.getNextNum() == game.getGrid()[END - 1][END] or
        game.getNextNum() == game.getGrid()[END - 1][END - 1] or
        game.getNextNum() == game.getGrid()[END][END - 1]):
        return game.placeNextNum(INVALID)
    game.pushValidLoc()
    return game.placeNextNum(game.getNextNum())

def left_edge(game, row, START):
    if (game.getNextNum() == game.getGrid()[row - 1][START] or
        game.getNextNum() == game.getGrid()[row + 1][START] or
        game.getNextNum() == game.getGrid()[row][START + 1] or
        game.getNextNum() == game.getGrid()[row - 1][START + 1] or
        game.getNextNum() == game.getGrid()[row + 1][START + 1]):
        return game.placeNextNum(INVALID)
    game.pushValidLoc()
    return game.placeNextNum(game.getNextNum())

def top_edge(game, column, START):
    if (game.getNextNum() == game.getGrid()[START][column - 1] or
        game.getNextNum() == game.getGrid()[START][column + 1] or
        game.getNextNum() == game.getGrid()[START + 1][column] or
        game.getNextNum() == game.getGrid()[START + 1][column - 1] or
        game.getNextNum() == game.getGrid()[START + 1][column + 1]):
        return game.placeNextNum(INVALID)
    game.pushValidLoc()
    return game.placeNextNum(game.getNextNum())

def right_edge(game, row, END):
    if (game.getNextNum() == game.getGrid()[row - 1][END] or
        game.getNextNum() == game.getGrid()[row + 1][END] or
        game.getNextNum() == game.getGrid()[row][END - 1] or
        game.getNextNum() == game.getGrid()[row - 1][END - 1] or
        game.getNextNum() == game.getGrid()[row + 1][END - 1]):
        return game.placeNextNum(INVALID)
    game.pushValidLoc()
    return game.placeNextNum(game.getNextNum())

def bottom_edge(game, column, END):
    if (game.getNextNum() == game.getGrid()[END][column - 1] or
        game.getNextNum() == game.getGrid()[END][column + 1] or
        game.getNextNum() == game.getGrid()[END - 1][column] or
        game.getNextNum() == game.getGrid()[END - 1][column - 1] or
        game.getNextNum() == game.getGrid()[END - 1][column + 1]):
        return game.placeNextNum(INVALID)
    game.pushValidLoc()
    return game.placeNextNum(game.getNextNum())

def middle_block(game, row, column):
    if (game.getNextNum() == game.getGrid()[row - 1][column] or
        game.getNextNum() == game.getGrid()[row + 1][column] or
        game.getNextNum() == game.getGrid()[row][column - 1] or
        game.getNextNum() == game.getGrid()[row][column + 1] or
        game.getNextNum() == game.getGrid()[row - 1][column - 1] or
        game.getNextNum() == game.getGrid()[row - 1][column + 1] or
        game.getNextNum() == game.getGrid()[row + 1][column - 1] or
        game.getNextNum() == game.getGrid()[row + 1][column + 1]):
        return game.placeNextNum(INVALID)
    game.pushValidLoc()
    return game.placeNextNum(game.getNextNum())
######### end of functions checking corners, edges, and middle blocks #######



# check location logic
def check_input(game, START, END):
    row = game.getLoc()[0]
    column = game.getLoc()[1]

    if (game.getGrid()[row][column] != 0):     #number already in location
            return game.placeNextNum(INVALID)

    ## CORNERS ##    
    if (row == START and column == START):   #TOP LEFT CORNER
        return top_left_corner(game, START)
        
    if (row == END and column == START):     #BOTTOM LEFT CORNER
        return bottom_left_corner(game, START, END)
        
    if (row == START and column == END):     #TOP RIGHT CORNER
        return top_right_corner(game, START, END)
        
    if (row == END and column == END):   #BOTTOM RIGHT CORNER
        return bottom_right_corner(game, END)

    ## EDGES ##
    if (column == START):   #LEFT EDGE
        return left_edge(game, row, START)

    if (row == START):   #TOP EDGE    
        return top_edge(game, column, START)

    if (column == END):     #RIGHT EDGE
        return right_edge(game, row, END)

    if (row == END):     #BOTTOM EDGE
        return bottom_edge(game, column, END)

    ## ANY OTHER BLOCK ##    
    return middle_block(game, row, column)



def main():
    game = Game()   #create the Game object

    #level select loop
    while True:
        print("Enter level for grid: ", end='')
        lineToRead = input()                    #get the level to play

        #ensure level input is an integer
        try:
            lineToRead = int(lineToRead)
        except(ValueError):
            os.system('cls')
            print("Invalid input: please enter a number.")
            continue
        else:
            game.setGridStart(getGrid(lineToRead))        #beginning state of the grid
            if (game.getGridStart() == -1):   return 0    #file not found, close app   
            if (game.getGridStart() == -2):   continue    #invalid level input; try again
            break                                         #valid input; continue


    game.setGrid()                           #grid for manipulation and display
    

    #main loop
    while (game.getNextNum() != 'q'):
        print(game.getValidLoc())
        print("(u)ndo, (r)eset, or (q)uit")
        print()
        game.printGrid()     #display the grid for user
        print("\nnumber to input: ", end='')
        game.setNextNum(input())

        #undo
        if (game.getNextNum() == 'u'):
            #nothing to undo
            if (len(game.getValidLoc()) == 0):
                os.system('cls')
                print("Nothing to undo")
                continue
            os.system('cls')
            game.undoGridPos()
            game.popValidLoc()
            print("UNDO")
            continue
        #reset
        if (game.getNextNum() == 'r'):
            game.resetGrid()
            os.system('cls')
            print("RESET")
            continue
        #quit
        if (game.getNextNum() =='q'):
            break


        #ensure that the inputted number is an integer
        try:
            game.setNextNum(int(game.getNextNum()))  
        except(ValueError):
            print("Invalid input. Please use a number in the range of 1 - 4.")
            continue
        #ensure inputted number is within range
        if (game.getNextNum() not in [1, 2, 3, 4]):
            print("Invalid input. Please use a number in the range of 1 - 4.")
            continue

        while True:
            print("row: ", end='')
            game.setLocRow(input())     #get row
            #ensure input is an integer
            try:
                game.setLocRow(int(game.getLoc()[0]))
            except(ValueError):
                print(f"Invalid input. Please use a number between 0 and {len(game.getGrid())-1}")
                continue
            #ensure input is within range
            if (game.getLoc()[0] not in range(0, len(game.getGrid()))):
                print(f"Invalid input. Please use a number between 0 and {len(game.getGrid())-1}.")
                continue
            break
        
        while True:
            print("column: ", end='')
            game.setLocColumn(input())  #get column
            #ensure input is an integer
            try:
                game.setLocColumn(int(game.getLoc()[1]))
            except(ValueError):
                print(f"Invalid input. Please use a number between 0 and {len(game.getGrid())-1}")
                continue
            #ensure input is within range
            if (game.getLoc()[1] not in range(0, len(game.getGrid()))):
                print(f"Invalid input. Please use a number between 0 and {len(game.getGrid())-1}.")
                continue
            break

                     
        os.system('cls')        
        output = check_input(game, 0, len(game.getGrid()) - 1) #begin processing user input
        if (output != INVALID):  #vaild placement
            game.setGridPos(output)

        if (game.checkGrid() != -1):    #finished grid
            game.printGrid()
            print("Grid Complete!")
            break

    print("Good-bye!")
    sleep(2)


if __name__ == "__main__":
    main()
