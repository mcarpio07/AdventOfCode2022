INPUT_FILE = './Day 10/input.txt'


intensity = 1
totalCicles = 0
sprite = list([intensity,intensity+1,intensity+2])
def updateSprite(intensity):
    sprite.clear()
    sprite.append(intensity)
    sprite.append(intensity+1)
    sprite.append(intensity+2)

def checkInterestingIntensity():
    global totalCicles  
    if totalCicles % 40 == 0:
        return True
    return False


def checkFinalCycle():
    global crt
    if checkInterestingIntensity():
        totalCrt.append(crt)
        crt = ''
    
def printCharacter():
    if totalCicles % 40 in sprite:
        return '##'
    return '  '

interestingIntensity = []
totalCrt = []
crt = ''
with open(INPUT_FILE) as file:
    for line in file.readlines():
        instruction = line.strip().split()
        if len(instruction) == 2:

            totalCicles += 1
            crt += printCharacter()
            checkFinalCycle()

            totalCicles += 1
            crt += printCharacter()
            checkFinalCycle()

            intensity += int (instruction[1])
            print(sprite)
            updateSprite(intensity)
        else:
            totalCicles += 1
            crt += printCharacter()
            checkFinalCycle()

for crt in totalCrt:
    print (crt)