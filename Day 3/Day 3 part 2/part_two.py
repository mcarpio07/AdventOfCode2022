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
    lines = file.readlines()
    i = 0
    while i < len(lines):
        bagOne = lines[i].replace('\n', '')

        try:
             bagTwo = lines[i+1].replace('\n', '')
             bagThree =lines[i+2].replace('\n', '')
        except IndexError:
            break

        commonItems = list(set(bagOne).intersection(bagTwo).intersection(bagThree))
        for item in commonItems:
            totalPriority += items[item]
        i += 3

print('Total Priority: %d' % totalPriority)