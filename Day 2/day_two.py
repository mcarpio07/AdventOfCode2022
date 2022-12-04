from enum import Enum

INPUT_FILE = './Day 2/input.txt'

class Movements(Enum):
    STONE = 'STONE'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'

ENEMY_MOVEMENT = {
    'A': Movements.STONE,
    'B': Movements.PAPER,
    'C': Movements.SCISSORS,
}

PLAYER_MOVEMENT = {
    'X': Movements.STONE,
    'Y': Movements.PAPER,
    'Z': Movements.SCISSORS,
}

MOVEMENT_SCORE = {
    Movements.STONE.value: 1,
    Movements.PAPER.value: 2,
    Movements.SCISSORS.value: 3
}

def play(enemy, player):
    if enemy == player:
        return 3
    elif (
       enemy == Movements.STONE.value and player == Movements.SCISSORS.value or
       enemy == Movements.SCISSORS.value and player == Movements.PAPER.value or
       enemy == Movements.PAPER.value and player == Movements.STONE.value
    ):
        return 0
    else:
        return 6

points = 0
with open(INPUT_FILE) as file:
    for line in file:
        game = line.replace('\n', '').split(' ')

        enemy = ENEMY_MOVEMENT.get(game[0]).value
        player = PLAYER_MOVEMENT.get(game[1]).value

        points += MOVEMENT_SCORE.get(player)
        points += play(enemy, player)


print('Total points: '+ str(points))




