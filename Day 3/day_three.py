import string

INPUT_FILE = './Day 3/input.txt'


def chargeItems():
    items = {}
    priority = 1
    letters = list(string.ascii_letters)
    for item in letters:
        items[item] = priority
        priority += 1

    return items



items = chargeItems()
totalPriority = 0
with open(INPUT_FILE) as file:
    for line in file:
        line = line.replace('\n', '')
        bagOne = line[:len(line)//2]
        bagTwo = line[len(line)//2:]
        commonItems = list(set(bagOne).intersection(bagTwo))
        for item in commonItems:
            totalPriority += items[item]

print('Total Priority: %d' % totalPriority)