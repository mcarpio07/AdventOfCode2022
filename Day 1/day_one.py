INPUT_FILE = './Day 1/input.txt'


maxCal = 0
actualCal = 0
cals = [] 
with open(INPUT_FILE) as file:
    for line in file:
        if line != '\n':
            actualCal += int(line)
        else:
            cals.append(actualCal)
            actualCal = 0
        if actualCal > maxCal:
            maxCal = actualCal

print("El elfo con mas calorias cuenta con un total de " + str(maxCal) + " calorias")

# Part 2
cals.sort(reverse = True)
threeMostCals = cals[:3]
print(threeMostCals)
print("La suma total de los tres elfos con mas calorias es: " + str(sum(threeMostCals)))