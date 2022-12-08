INPUT_FILE = './Day 6/input.txt'

# FOR PART TWO, CHANGE THIS VALUE, FROM 4 TO 14
LENGTH_OF_FLOW = 4

def checkFlow(flow):
    setFlow = set(flow)
    if (len(setFlow) == LENGTH_OF_FLOW):
        return True
    return False

with open(INPUT_FILE) as file:
    line = file.readlines()[0]
    flow = []
    numFlow = 0
    for letter in line:
        if len(flow) == LENGTH_OF_FLOW:
            if checkFlow(flow):
                break
            else:
                flow.pop(0)
                flow.append(letter)
                numFlow += 1
        else:
            flow.append(letter)
            numFlow += 1

            
print ("Num of flow: ", numFlow)