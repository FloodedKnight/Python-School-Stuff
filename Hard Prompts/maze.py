# !!!!!!!!!!!!
# Basically, this finds all the possible paths from one point to another, not taking in account for walls
# Then, it goes back to the originalMaze and loops all the paths, and if there is a wall in that list it removes it.
# Then, i just find the list with the shortest length, and that is the shorest path.
# !!!!!!!!!!!!


originalMaze = [
  [0, 1, 0, 0, 0],
  [0, 1, 0, 1, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 1, 0, 0]
]

# originalMaze = [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]


start = (0, 0) # !!! I FLIPPED THE COORDINATES THE WHOLE TIME, TOO LAZY TO CHANGE AFTER
end = (1, 0) # !!! I FLIPPED THE COORDINATES THE WHOLE TIME, TOO LAZY TO CHANGE AFTER
maze = originalMaze[:]

#! ---------------------- EDIT THIS IF YOU DONT WANT TO INCLUDE DIAGNAL MOVES
moves = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
allPaths = []

def getMoves(loc, path=[]):
    possibleMoves = []
    x, y = loc
    #* check if were at end
    if loc == end:
        allPaths.append(path + [loc])
        return
    
    # ! MARK AS WALL SINCE WE'VE BEEN THERE BEFORE
    maze[x][y] = 1
    # * check the next move
    for moveX, moveY in moves:
        #! REMOVE NEGATIVE INDEX
        if ((x + moveX) < 0) or ((y + moveY) < 0):
            continue
        try:
            #* coordinate of next move
            newCoord = (x + moveX, y + moveY)
            val = maze[newCoord[0]][newCoord[1]]
            #* make sure we didnt hit a wall
            if val == 0:
                possibleMoves.append((newCoord))
        except(IndexError):
            continue

    #* loop the new possible moves
    for i in possibleMoves:
        #* get the moves of the new moves
        getMoves(i, path + [loc])
    
    maze[x][y] = 0

getMoves(start)
validPaths = [path for path in allPaths if all(originalMaze[x][y] == 0 for (x, y) in path)]
for path in allPaths:
    if all(originalMaze[x][y] == 0 for (x, y) in path):
        validPaths.append(path)
try:
    print(f'Shortest path is from: {min(validPaths, key=len)} with {len(min(validPaths, key=len))} points / {len(min(validPaths, key=len)) - 1} steps.')
except:
    print("No path found")
