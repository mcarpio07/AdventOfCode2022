INPUT_FILE = './Day 9/input.txt'


LEFT = 'L'
RIGHT = 'R'
UP = 'U'
DOWN = 'D'
MAX_DIST = 2
positionsT = {tuple([0,0])}
posH = {
    'x': 0,
    'y': 0
}
posT = {
    'x': 0,
    'y': 0
}
def moveH(direction, numSteps):
    while numSteps > 0:
        if direction == LEFT:
            posH['x'] = posH['x'] - 1
            moveT()
        if direction == RIGHT:
            posH['x'] = posH['x'] + 1
            moveT()
        if direction == UP:
            posH['y'] = posH['y'] + 1
            moveT()
        if direction == DOWN:
            posH['y'] = posH['y'] - 1
            moveT()
        numSteps = numSteps - 1

def moveT():
    #DIAGONAL ↗
    if (
        (posT['y'] - posH['y'] == -MAX_DIST and
        posT['x'] - posH['x'] == -1)
        or
        (posT['y'] - posH['y'] == -1 and
        posT['x'] - posH['x'] == -MAX_DIST)
    ):
        posT['y'] = posT['y']+1
        posT['x'] = posT['x']+1
        positionsT.add(tuple([posT['x'], posT['y']]))

    #DIAGONAL ↘
    if (
        (posT['y'] - posH['y'] == MAX_DIST and
        posT['x'] - posH['x'] == -1)
        or
        (posT['y'] - posH['y'] == 1 and
        posT['x'] - posH['x'] == -MAX_DIST)
    ):
        posT['y'] = posT['y']-1
        posT['x'] = posT['x']+1

    #DIAGONAL ↖
    if (
        (posT['y'] - posH['y'] == -MAX_DIST and
        posT['x'] - posH['x'] == 1)
        or
        (posT['y'] - posH['y'] == -1 and
        posT['x'] - posH['x'] == MAX_DIST)
    ):
        posT['y'] = posT['y']+1
        posT['x'] = posT['x']-1
    
    #DIAGONAL ↙
    if (
        (posT['y'] - posH['y'] == MAX_DIST and
        posT['x'] - posH['x'] == 1)
        or
        (posT['y'] - posH['y'] == 1 and
        posT['x'] - posH['x'] == MAX_DIST)
    ):
        posT['y'] = posT['y']-1
        posT['x'] = posT['x']-1
    
    #VERTICAL
    if posT['y'] - posH['y'] == -MAX_DIST:
        posT['y'] = posT['y']+1
    
    if posT['y'] - posH['y'] == MAX_DIST:
        posT['y'] = posT['y']-1
    
    #HORIZONTAL
    if posT['x'] - posH['x'] == -MAX_DIST:
        posT['x'] = posT['x']+1
    
    if posT['x'] - posH['x'] == MAX_DIST:
        posT['x'] = posT['x']-1
    
    positionsT.add(tuple([posT['x'], posT['y']]))

with open(INPUT_FILE) as file:
    for line in file.readlines():
        movement = line.strip().split()
        moveH(movement[0], int(movement[1]))


print("Total visits: ", len(positionsT))