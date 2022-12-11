INPUT_FILE = './Day 9/input.txt'


LEFT = 'L'
RIGHT = 'R'
UP = 'U'
DOWN = 'D'
MAX_DIST = 2
positionsT = {tuple([0,0])}
H = {'x': 0,'y': 0}
one = {'x': 0,'y': 0}
two = {'x': 0,'y': 0}
three = {'x': 0,'y': 0}
four = {'x': 0,'y': 0}
five = {'x': 0,'y': 0}
six = {'x': 0,'y': 0}
seven = {'x': 0,'y': 0}
eight = {'x': 0,'y': 0}
nine = {'x': 0,'y': 0}
def moveH(direction, numSteps):
    while numSteps > 0:
        if direction == LEFT:
            H['x'] = H['x'] - 1
            moveKnots()
        if direction == RIGHT:
            H['x'] = H['x'] + 1
            moveKnots()
        if direction == UP:
            H['y'] = H['y'] + 1
            moveKnots()
        if direction == DOWN:
            H['y'] = H['y'] - 1
            moveKnots()
        numSteps = numSteps - 1

def move(knot, previousKnot):
    #DIAGONAL ↗
    if (
        (knot['y'] - previousKnot['y'] == -MAX_DIST and
        knot['x'] - previousKnot['x'] == -1)
        or
        (knot['y'] - previousKnot['y'] == -1 and
        knot['x'] - previousKnot['x'] == -MAX_DIST)
    ):
        knot['y'] = knot['y']+1
        knot['x'] = knot['x']+1

    #DIAGONAL ↘
    if (
        (knot['y'] - previousKnot['y'] == MAX_DIST and
        knot['x'] - previousKnot['x'] == -1)
        or
        (knot['y'] - previousKnot['y'] == 1 and
        knot['x'] - previousKnot['x'] == -MAX_DIST)
    ):
        knot['y'] = knot['y']-1
        knot['x'] = knot['x']+1

    #DIAGONAL ↖
    if (
        (knot['y'] - previousKnot['y'] == -MAX_DIST and
        knot['x'] - previousKnot['x'] == 1)
        or
        (knot['y'] - previousKnot['y'] == -1 and
        knot['x'] - previousKnot['x'] == MAX_DIST)
    ):
        knot['y'] = knot['y']+1
        knot['x'] = knot['x']-1
    
    #DIAGONAL ↙
    if (
        (knot['y'] - previousKnot['y'] == MAX_DIST and
        knot['x'] - previousKnot['x'] == 1)
        or
        (knot['y'] - previousKnot['y'] == 1 and
        knot['x'] - previousKnot['x'] == MAX_DIST)
    ):
        knot['y'] = knot['y']-1
        knot['x'] = knot['x']-1
    
    #VERTICAL
    if knot['y'] - previousKnot['y'] == -MAX_DIST:
        knot['y'] = knot['y']+1
    
    if knot['y'] - previousKnot['y'] == MAX_DIST:
        knot['y'] = knot['y']-1
    
    #HORIZONTAL
    if knot['x'] - previousKnot['x'] == -MAX_DIST:
        knot['x'] = knot['x']+1
    
    if knot['x'] - previousKnot['x'] == MAX_DIST:
        knot['x'] = knot['x']-1
    
    if knot == nine:
        positionsT.add(tuple([knot['x'], knot['y']]))

def moveKnots():
    move(one,H)
    move(two,one)
    move(three,two)
    move(four,three)
    move(five,four)
    move(six,five)
    move(seven,six)
    move(eight,seven)
    move(nine,eight)

with open(INPUT_FILE) as file:
    for line in file.readlines():
        movement = line.strip().split()
        moveH(movement[0], int(movement[1]))

print("Total visits: ", len(positionsT))