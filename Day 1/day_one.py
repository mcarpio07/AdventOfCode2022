INPUT_FILE = './Day 1/input.txt'


maxCal = 0
actualCal = 0
with open(INPUT_FILE) as file:
    for line in file:
        if line != '\n':
            actualCal += int(line)
        else:
            actualCal = 0
        if actualCal > maxCal:
            maxCal = actualCal

print("El elfo con mas calorias cuenta con un total de " + str(maxCal) + " calorias")