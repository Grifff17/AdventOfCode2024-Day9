#reads in file
def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

#adds two xy coordinates together
def posAdd(pos1, pos2):
    return tuple([ a+b for a,b in zip(pos1, pos2) ])

#subtracts two xy coordinates
def posSub(pos1, pos2):
    return tuple([ a-b for a,b in zip(pos1, pos2) ])

#multiplies two xy coordinates together
def posMult(pos1, pos2):
    return tuple([ a*b for a,b in zip(pos1, pos2) ])

#checks if a xy coordinate is within a grid
def inGrid(pos, grid):
    return pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0])

#find the xy coordinate of a value in a grid
def findInGrid(grid, target):
    for i, row in enumerate(grid):
            if target in row:
                return (i, row.index(target))