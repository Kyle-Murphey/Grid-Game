import numpy as np

class Game:
    def __init__(self):
        self.loc = [-1, -1]                 #location on grid
        self.valid_loc = list()             #record of locations
        self.grid_start = np.array([[]])    #beginning state of grid
        self.grid = np.array([[]])          #grid for manipulation and display 
        self.next_num = 0                   #number to be inserted into grid

    ## return the inputted location
    def getLoc(self):
        return self.loc

    ## set the row in the loc variable
    def setLocRow(self, row):
        self.loc[0] = row

    ## set the column in the loc variable
    def setLocColumn(self, column):
        self.loc[1] = column


    ## return the list of valid locations used
    def getValidLoc(self):
        return self.valid_loc

    ## add a new valid location to the list
    def pushValidLoc(self):
        self.valid_loc.append(self.loc[:])
    
    ## remove a valid location from the list after an undo
    def popValidLoc(self):
        self.valid_loc.pop()


    ## return the beginning grid arrangement
    def getGridStart(self):
        return self.grid_start

    ## set the beginning state of the grid
    def setGridStart(self, grid_start):
        self.grid_start = grid_start

    ## return the grid in use
    def getGrid(self):
        return self.grid

    ## set the grid to an array equal to the beginning state of the grid
    def setGrid(self):
        self.grid = np.array([row[:] for row in self.grid_start])
    
    ## set the position at loc to the value of next_num
    def setGridPos(self, next_num):
        self.grid[self.loc[0], self.loc[1]] = next_num

    ## undo the last insertion performed on the grid, and remove the last valid location
    def undoGridPos(self):
        end_of_list = len(self.valid_loc) - 1
        self.grid[self.valid_loc[end_of_list][0], self.valid_loc[end_of_list][1]] = 0
    
    ## reset the valid location list and reset the grid back to its beginning state
    def resetGrid(self):
        self.valid_loc.clear()
        self.grid = np.array([row[:] for row in self.grid_start])
        return self.grid
    
    ## display the grid
    def printGrid(self):
        i = 0
        for m in self.grid:
            for n in self.grid[i]:
                print(n, sep=' ', end=' ')
            print()
            i += 1
    
    ## check if all locations are filled and the grid is complete
    def checkGrid(self):
        i = 0
        for m in self.grid:
            for n in self.grid[i]:
                if (n == 0):
                    return -1
            i += 1
        return 0

    
    ## return the number inputted by the user for insertion
    def getNextNum(self):
        return self.next_num

    ## set the next_num variable to the user input
    def setNextNum(self, next_num):
        self.next_num = next_num

    ## determine if user input can be inserted at given location, -1 is equivalant to an invalid location for the number to be inserted
    def placeNextNum(self, next_num):
        if (next_num == -1):
            print(f"{self.next_num} CAN NOT BE PLACED AT {self.loc}")
        else:
            print(f"{self.next_num} PLACED AT {self.loc}")
        return next_num