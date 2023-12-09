global digits
digits = '1234567890'

def dataOrganizer(rawData):
    outputData = []
    for line in rawData:
        outputData.append([letter for letter in line])
    return outputData

def symbolFinder(organizedData):
    notSymbols = '.123456789'
    positions = []
    for line in organizedData:
        for index, symbol in enumerate(line):
            if symbol in notSymbols: continue
            else: positions.append({
                'symbol': symbol,
                'line': organizedData.index(line),
                'index': index
            })
    return positions

def numberRebuilder(line,index):
    focusLine = organizedData[line]
    maxLine = len(organizedData[0]) - 1
    startingIndex = index
    while True:
        if focusLine[startingIndex] not in digits:
            startingIndex += 1
            break
        else:
            startingIndex -= 1
            if startingIndex == 0:
                startingIndex += 1
                break

    number = ''
    index = startingIndex
    while True:
        if focusLine[index] not in digits:
            break
        else:
            number += focusLine[index]
            index += 1
            if index > maxLine: break

    return {
        'number': int(number),
        'line': line,
        'index': (startingIndex, startingIndex + len(number) - 1)
    }

def numberFinder(organizedData):
    numbersFound = []
    currentNumber = ''
    for lineIndex, lineData in enumerate(organizedData):
        if currentNumber != '': numbersFound.append({
                    'number': int(currentNumber),
                    'line': lineIndex-1,
                    'index': (maxLine + 1 - len(currentNumber), maxLine)
                })
        maxLine = len(lineData)-1
        currentNumber = ''
        for symbolIndex, symbol in enumerate(lineData):
            if symbol in digits:
                currentNumber += symbol
            elif symbol not in digits and len(currentNumber) != 0:
                numbersFound.append({
                    'number': int(currentNumber),
                    'line': lineIndex,
                    'index': (symbolIndex - len(currentNumber), symbolIndex-1)
                })
                currentNumber = ''
            else: continue
    return numbersFound

def uniqueValues(list:list):
    uniqueList = []
    for entry in list:
        if entry not in uniqueList:
            uniqueList.append(entry)
    return uniqueList

def task1():
    maxLength = len(organizedData[0]) - 1
    maxRows = len(organizedData) - 1
    numbers = numberFinder(organizedData)
    t1counter = 0
    for entry in numbers:
        number = entry['number']
        line = entry['line']
        leftBorder = entry['index'][0]
        rightBorder = entry['index'][1]
        possibleSymbolPositions = []
        for n in range(line-1 if line>0 else line, (line+1 if line<maxRows else maxRows)+1):
            if n == line:
                if leftBorder != 0: possibleSymbolPositions.append((line,leftBorder-1))
                if rightBorder != maxLength: possibleSymbolPositions.append((line,rightBorder+1))
            else:
                for m in range(leftBorder -1 if leftBorder != 0 else 0, (rightBorder+1 if rightBorder != maxLength else maxLength) + 1):
                    possibleSymbolPositions.append((n,m))
        valid = False
        for symbol in possibleSymbolPositions:
            if valid == True: continue
            line = symbol[0]
            index = symbol[1]
            notSymbols = '.1234567890'
            if organizedData[line][index] not in notSymbols: valid = True
            else: continue
        if valid == True: t1counter += number
    return t1counter

def task2():
    gearRatioCounter = 0
    symbols = symbolFinder(organizedData)
    possibleGears = [symbol for symbol in symbols if symbol['symbol'] == '*']
    for gear in possibleGears:
        line = gear['line']
        index = gear['index']
        possibleNumberPositions = []
        maxLength = len(organizedData[0]) - 1
        maxRows = len(organizedData) - 1
        for n in range(line-1 if line>0 else line, (line+1 if line<maxRows else maxRows)+1):
            if n == line:
                if index != 0: possibleNumberPositions.append((line,index-1))
                if index != maxLength: possibleNumberPositions.append((line,index+1))
            else:
                for m in range(index -1 if index != 0 else 0, (index+1 if index != maxLength else maxLength) + 1):
                    possibleNumberPositions.append((n,m))
        adjacentNumbers = []
        for entry in possibleNumberPositions:
            line = entry[0]
            index = entry[1]
            if organizedData[line][index] not in digits:
                continue
            adjacentNumbers.append(numberRebuilder(line,index))
        adjacentNumbers = uniqueValues(adjacentNumbers)
        if len(adjacentNumbers) == 2: 
            gearRatioCounter += adjacentNumbers[0]['number'] * adjacentNumbers[1]['number']
    return gearRatioCounter
        


with open('input\\day3') as inputFile:
    rawData = [line.strip() for line in inputFile.readlines()]

global organizedData
organizedData = dataOrganizer(rawData)

#TASK 1
print(f'TASK 1 -> {task1()}')

#TASK 2 
print(f'TASK 2 -> {task2()}')