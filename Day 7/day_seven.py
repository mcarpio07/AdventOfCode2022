INPUT_FILE = './Day 7/input.txt'


fileSizes = {}
CD_ORDER = 'cd'
BEFORE_DIR = '..'
ORDER = '$'
IS_DIR = 'dir'
total = 0
with open(INPUT_FILE) as file:
    sizeDir = 0
    for line in reversed(file.readlines()):
        arrayLine = line.strip().split(' ')
        if ORDER not in arrayLine and IS_DIR not in arrayLine:
            try:
                sizeDir += int(arrayLine[0])
            except:
                continue
        elif IS_DIR in arrayLine:
            try:
                sizeDir += fileSizes[arrayLine[1]]
            except:
                continue
        elif CD_ORDER in arrayLine and BEFORE_DIR not in arrayLine: 
            directory = arrayLine[2]
            fileSizes[directory] = sizeDir
            if sizeDir <= 100000:
                total += sizeDir
            sizeDir = 0


print ("total size of directorys <= 100000: ", total)