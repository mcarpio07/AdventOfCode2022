INPUT_FILE = './Day 4/input.txt'


def chargeRange(interval):
    if(interval[0] == interval[1]):
        return [int(interval[0])]

    return list(range(int(interval[0]), int(interval[1])+1))

def intersection_list(list1, list2):  
   list3 = [value for value in list1 if value in list2]  
   return list3  

pairWithoutOverlapping = 0
totalRounds = 0
with open(INPUT_FILE) as file:
    for line in file:
        totalRounds += 1
        ranges = line.replace('\n', '').split(',')
        intervalOne = ranges[0].split('-')
        intervalTwo = ranges[1].split('-')
        rangeOne = chargeRange(intervalOne)
        rangeTwo = chargeRange(intervalTwo)
        commons = intersection_list(rangeOne, rangeTwo)
        if len(commons) == 0:
            pairWithoutOverlapping += 1
    
    numOverlap = totalRounds - pairWithoutOverlapping

print('Num of total overlapping intervals: %d' % numOverlap)