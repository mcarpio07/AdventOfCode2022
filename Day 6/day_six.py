INPUT_FILE = './Day 6/input.txt'


def checkFlow(flow):
    setFlow = set(flow)
    if (len(setFlow) == 4):
        return True
    return False

with open(INPUT_FILE) as file:
    line = file.readlines()[0]
    flow = []
    numFlow = 0
    for letter in line:
        if len(flow) == 4:
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