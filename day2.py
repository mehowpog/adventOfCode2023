class Game:
    def __init__(self, id:int, rounds:tuple):
        self.id = id
        self.rounds = rounds

    def maxBalls(self):
        rounds = self.rounds
        redMax = max([round['red'] for round in rounds])
        greenMax = max([round['green'] for round in rounds])
        blueMax = max([round['blue'] for round in rounds])
        return {
            'red': redMax,
            'green': greenMax,
            'blue': blueMax
        }

def gamesPrint():
    for game in dataOrganizer(rawData):
        print(f'Game {game.id}:')
        for round in game.rounds:
            print(f'    {round}')
        print(f'    maxballs -> {game.maxBalls()}')

def dataOrganizer(rawData):
    games = []
    for line in rawData:
        colonSplit = line.split(':')
        id = int(colonSplit[0].replace('Game ', ''))
        roundsRaw = [line.strip() for line in colonSplit[1].split(';')]
        rounds = []
        for round in roundsRaw:
            red = 0
            green = 0
            blue = 0
            balls = [line.split() for line in round.split(',')]
            for entry in balls:
                match (entry[1]):
                    case 'red': red += int(entry[0])
                    case 'green': green += int(entry[0])
                    case 'blue': blue += int(entry[0])
            rounds.append({
                'red': red,
                'green': green,
                'blue': blue
            })
        games.append(Game(id, rounds))
    return games

with open('input\\day2') as inputFile:
    rawData = [line.strip() for line in inputFile.readlines()]

games = dataOrganizer(rawData)
gamesPrint()

#TASK 1
validCounter = 0
for game in games:
    maxBalls = game.maxBalls()
    if maxBalls['red'] > 12 or maxBalls['green'] > 13 or maxBalls['blue'] > 14:
        continue
    else: validCounter += game.id

print(f'TASK 1: {validCounter}')

#TASK 2
powerCounter = 0
for game in games:
    maxBalls = game.maxBalls()
    power = maxBalls['red'] * maxBalls['green'] * maxBalls['blue']
    powerCounter += power

print(f'TASK 2: {powerCounter}')
