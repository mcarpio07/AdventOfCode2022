INPUT_FILE = './Day 4/input.txt'


def chargeRange(interval):
    if(interval[0] == interval[1]):
        return [int(interval[0])]

    return list(range(int(interval[0]), int(interval[1])+1))

def intersection_list(list1, list2):  
   list3 = [value for value in list1 if value in list2]  
   return list3  

totalPair = 0
with open(INPUT_FILE) as file:
    for line in file:
        ranges = line.replace('\n', '').split(',')
        intervalOne = ranges[0].split('-')
        intervalTwo = ranges[1].split('-')
        rangeOne = chargeRange(intervalOne)
        rangeTwo = chargeRange(intervalTwo)
        commons = intersection_list(rangeOne, rangeTwo)
        if (
            len(commons) > 0 and
            (commons == rangeOne or commons == rangeTwo)
        ):
            totalPair += 1

print('Num of total of repeat pairs: %d' % totalPair)