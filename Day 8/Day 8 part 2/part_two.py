INPUT_FILE = './Day 8/input.txt'


def chargeMatrix(lines):
    matrix = []
    for trees in lines:
        fil = []
        for hight in trees.strip():
            fil.append(int(hight))
        matrix.append(fil)
    return matrix

def calculateTrees(matrix, fil, col):
    height = matrix[fil][col]
    numLeft = 0
    numRight = 0
    numUp = 0
    numDown = 0

    #FILE LEFT 
    for tree in reversed(matrix[fil][:col]):
        numLeft += 1
        if tree >= height: 
            break

    #FILE RIGHT
    for tree in matrix[fil][1+col:]:
        numRight += 1
        if tree >= height: 
            break

    #COLUMN UP
    for j in reversed(range(fil)):
        numUp += 1
        num = matrix[j][col]
        if num >= height:
            break

    #COLUMN DOWN
    for j in range(fil+1,len(matrix[fil])):
        numDown += 1
        num = matrix[j][col]
        if num >= height:
            break

    return numLeft * numRight * numUp * numDown


def letsPlay(matrix):
    maxScore = 0
    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix[0])-1):
            scoreTrees = calculateTrees(matrix, i, j)
            if scoreTrees > maxScore:
                maxScore = scoreTrees
    return maxScore


with open(INPUT_FILE) as file:
    lines = file.readlines()
    matrix = chargeMatrix(lines)
    maxScore = letsPlay(matrix)
    
print("Max score trees: ", maxScore)