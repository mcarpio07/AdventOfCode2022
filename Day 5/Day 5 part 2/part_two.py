INPUT_FILE = './Day 5/input.txt'

MOVE_WORD = 'move'
FROM_WORD = 'from'
TO_WORD = 'to'
heap = {
    1: ['Q','S','W','C','Z','V','F','T'],
    2: ['Q','R','B'],
    3: ['B','Z','T','Q','P','M','S'],
    4: ['D','V','F','R','Q','H'],
    5: ['J','G','L','D','B','S','T','P'],
    6: ['W','R','T','Z'],
    7: ['H','Q','M','N','S','F','R','J'],
    8: ['R','N','F','H','W'],
    9: ['J','Z','T','Q','P','R','B']
}

def move(numBoxes,fromHeap, toHeap):
    boxes = heap[fromHeap][-numBoxes:]
    del heap[fromHeap][-numBoxes:]
    heap[toHeap] = heap[toHeap] + boxes


with open(INPUT_FILE) as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if(MOVE_WORD in line):
            movement = list(map(int,line.replace(MOVE_WORD,'').replace(FROM_WORD,'-').replace(TO_WORD,'-').split('-')))
            numBoxes = movement[0]
            fromHeap = movement[1]
            toHeap = movement[2]
            move(numBoxes, fromHeap, toHeap)
    
    print('Last Boxes: ')
    for key in heap:
        print(heap[key].pop())
