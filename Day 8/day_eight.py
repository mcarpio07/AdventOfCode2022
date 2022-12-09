INPUT_FILE = './Day 8/input.txt'


def chargeMatrix(lines):
    matrix = []
    for trees in lines:
        fil = []
        for hight in trees.strip():
            fil.append(int(hight))
        matrix.append(fil)
    return matrix

def getNumBorder(matrix):
    numBorder = len(matrix[0])
    numBorder += len(matrix[-1])
    for i in range(2, len(matrix)): numBorder += 2
    return  numBorder

def checkVisible(matrix, fil, col):
    height = matrix[fil][col]
    visible = True

    #FILE LEFT 
    for tree in matrix[fil][:col]:
        if tree >= height: 
            visible = False
            break
    if visible:
        return True

    #FILE RIGHT
    visible = True 
    for tree in matrix[fil][1+col:]:
        if tree >= height: 
            visible = False
            break
    if visible:
        return True

    #COLUMN UP
    visible = True
    for j in range(fil):
        num = matrix[j][col]
        if num >= height:
            visible = False
            break
    if visible:
        return True

    #COLUMN DOWN
    visible = True
    for j in range(fil+1,len(matrix[fil])):
        num = matrix[j][col]
        if num >= height:
            visible = False
            break
    if visible:
        return True

    return visible


def letsPlay(matrix):
    numVisibleTrees = getNumBorder(matrix)
    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix[0])-1):
            if checkVisible(matrix, i, j):
                numVisibleTrees += 1
    return numVisibleTrees


with open(INPUT_FILE) as file:
    lines = file.readlines()
    matrix = chargeMatrix(lines)
    numVisibleTrees = letsPlay(matrix)
    
print("Total visible trees: ", numVisibleTrees)