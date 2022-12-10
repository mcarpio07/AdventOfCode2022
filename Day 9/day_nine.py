INPUT_FILE = './Day 9/input.txt'


HEAP = 'H'
TAIL = 'T'
LEFT = 'L'
RIGHT = 'R'
UP = 'U'
DOWN = 'D'
TAM_MAP = 25
MAX_DIST = 2
VISITED = '#'
def chargeMap():
    map = []
    for i in range(TAM_MAP):
        file = []
        for j in range(TAM_MAP):
            file.append(".")
        map.append(file)
    map[10][10] = 'H'
    return map

def visualizeMap(map):
    print("Result Map:")
    for fila in map:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

def getH():
    posH = {}
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == HEAP:
                posH['fil'] = i
                posH['col'] = j
                break
    return posH

def getT():
    posT = {}
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == TAIL:
                posT['fil'] = i
                posT['col'] = j
                break
    return posT

def moveH(map, direction, numSteps, firstMovement):
    posH = getH()
    if direction == LEFT:
        map[posH['fil']][posH['col']] = TAIL if firstMovement else '.'
        if getT() == {} and not firstMovement:
            map[posH['fil']][posH['col']] = TAIL

        map[posH['fil']][posH['col']-numSteps] = HEAP

    if direction == RIGHT:
        map[posH['fil']][posH['col']] = TAIL if firstMovement else '.'
        if getT() == {} and not firstMovement:
            map[posH['fil']][posH['col']] = TAIL
        map[posH['fil']][posH['col']+numSteps] = HEAP
    
    if direction == UP:
        map[posH['fil']][posH['col']] = TAIL if firstMovement else '.'
        if getT() == {} and not firstMovement:
            map[posH['fil']][posH['col']] = TAIL
        map[posH['fil']-numSteps][posH['col']] = HEAP
    
    if direction == DOWN:
        map[posH['fil']][posH['col']] = TAIL if firstMovement else '.'
        if getT() == {} and not firstMovement:
            map[posH['fil']][posH['col']] = TAIL
        map[posH['fil']+numSteps][posH['col']] = HEAP

def checkMoveT(movement):
    posH = getH()
    posT = getT()
    if (
        abs(posT['fil'] - posH['fil']) >= 2 or
        abs(posT['col'] - posH['col']) >= 2
    ):
        return True
    return False

def moveT(map):
    posH = getH()
    posT = getT()
    if posT == {}: posT = posH
    #DIAGONAL ↗
    if (
        (posT['fil'] - posH['fil'] == MAX_DIST and
        posT['col'] - posH['col'] == -1)
        or
        (posT['fil'] - posH['fil'] == 1 and
        posT['col'] - posH['col'] == -MAX_DIST)
    ):
        map[posT['fil']][posT['col']] = VISITED
        map[posT['fil']-1][posT['col']+1] = TAIL
        return 
    
    #DIAGONAL ↘
    if (
        (posT['fil'] - posH['fil'] == -MAX_DIST and
        posT['col'] - posH['col'] == -1)
        or
        (posT['fil'] - posH['fil'] == -1 and
        posT['col'] - posH['col'] == -MAX_DIST)
    ):
        map[posT['fil']][posT['col']] = VISITED
        map[posT['fil']+1][posT['col']+1] = TAIL
        return
    
    #DIAGONAL ↖
    if (
        (posT['fil'] - posH['fil'] == MAX_DIST and
        posT['col'] - posH['col'] == 1)
        or
        (posT['fil'] - posH['fil'] == 1 and
        posT['col'] - posH['col'] == MAX_DIST)
    ):
        map[posT['fil']][posT['col']] = VISITED
        map[posT['fil']-1][posT['col']-1] = TAIL
        return
    
    #DIAGONAL ↙
    if (
        (posT['fil'] - posH['fil'] == -MAX_DIST and
        posT['col'] - posH['col'] == 1)
        or
        (posT['fil'] - posH['fil'] == -1 and
        posT['col'] - posH['col'] == MAX_DIST)
    ):
        map[posT['fil']][posT['col']] = VISITED
        map[posT['fil']+1][posT['col']-1] = TAIL
        return

    #VERTICAL
    if posT['fil'] - posH['fil'] == MAX_DIST:
        map[posT['fil']][posT['col']] = VISITED
        map[posT['fil']-1][posT['col']] = TAIL
        return

    if posT['fil'] - posH['fil'] == -MAX_DIST:
        map[posT['fil']][posT['col']] = VISITED
        map[posT['fil']+1][posT['col']] = TAIL
        return

    #HORIZONTAL
    if posT['col'] - posH['col'] == MAX_DIST:
        map[posT['fil']][posT['col']] = VISITED
        map[posT['fil']][posT['col']-1] = TAIL
        return

    if posT['col'] - posH['col'] == -MAX_DIST:
        map[posT['fil']][posT['col']] = VISITED
        map[posT['fil']][posT['col']+1] = TAIL
        return


with open(INPUT_FILE) as file:
    map = chargeMap()
    visualizeMap(map)
    firstMovement = True
    for line in file.readlines():
        movement = line.strip().split()
        moveH(map, movement[0], int(movement[1]), firstMovement)
        firstMovement = False
        moveT(map)
        visualizeMap(map)
