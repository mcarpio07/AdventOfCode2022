from enum import Enum

INPUT_FILE = './Day 2/input.txt'

class Movements(Enum):
    STONE = 'STONE'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'

class Result(Enum):
    WIN = 'WIN'
    DRAFT = 'DRAFT'
    LOSE = 'LOSE'

ENEMY_MOVEMENT = {
    'A': Movements.STONE,
    'B': Movements.PAPER,
    'C': Movements.SCISSORS,
}

GAME_RESULT = {
    'X': Result.LOSE,
    'Y': Result.DRAFT,
    'Z': Result.WIN,
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

def calculateMovement(enemy, result):
    if result == Result.DRAFT.value:
        return enemy
    if result == Result.LOSE.value:
        if enemy == Movements.SCISSORS.value:
            return Movements.PAPER.value
        if enemy == Movements.STONE.value:
            return Movements.SCISSORS.value
        if enemy == Movements.PAPER.value:
            return Movements.STONE.value
    if result == Result.WIN.value:
        if enemy == Movements.SCISSORS.value:
            return Movements.STONE.value
        if enemy == Movements.STONE.value:
            return Movements.PAPER.value
        if enemy == Movements.PAPER.value:
            return Movements.SCISSORS.value
    


points = 0
with open(INPUT_FILE) as file:
    for line in file:
        game = line.replace('\n', '').split(' ')

        enemy = ENEMY_MOVEMENT.get(game[0]).value
        result = GAME_RESULT.get(game[1]).value
        player = calculateMovement(enemy, result)

        points += MOVEMENT_SCORE.get(player)
        points += play(enemy, player)


print('Total points: '+ str(points))




