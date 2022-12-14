INPUT_FILE = './Day 10/input.txt'


intensity = 1
numCicles = 0
totalCicles = 0
def checkInterestingIntensity():
    global numCicles
    global totalCicles
    if totalCicles == 20:
        numCicles = 0
        return True
    if numCicles == 40:
        numCicles = 0
        return True
    return False

interestingIntensity = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        instruction = line.strip().split()
        if len(instruction) == 2:
            numCicles += 1
            totalCicles += 1
            if checkInterestingIntensity(): interestingIntensity.append(intensity*totalCicles)
            numCicles += 1
            totalCicles += 1
            if checkInterestingIntensity(): interestingIntensity.append(intensity*totalCicles)
            intensity += int (instruction[1])
        else:
            numCicles += 1
            totalCicles += 1
            if checkInterestingIntensity(): interestingIntensity.append(intensity*totalCicles)

print ('Interesting intensity:', sum(interestingIntensity))