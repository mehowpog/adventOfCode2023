def task1(line:str):
    digits = '123456789'
    for letter in line:
        if letter in digits:
            n1 = letter
            break
    for letter in line[::-1]:
        if letter in digits:
            n2 = letter
            break
    return int(n1+n2)

def task2(line:str):
    ogString = line
    reversedString = line[::-1]
    digits = '123456789'
    translation = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    backwardTranslation = {}
    for key in translation:
        backwardTranslation[key[::-1]] = translation[key]
    
    temp = ''
    while True:
        letter = ogString[len(temp)]
        if letter in digits:
            n1 = letter
            break
        else:
            temp += letter
            possibilities = [key for key in translation if key.startswith(temp)]
            if len(possibilities) == 0:
                ogString = ogString[1:]
                temp = ''
                continue
            
            if temp in possibilities:
                n1 = translation[temp]
                break
            else:
                continue

    temp = ''
    while True:
        letter = reversedString[len(temp)]
        if letter in digits:
            n2 = letter
            break
        else:
            temp += letter
            possibilities = [key for key in backwardTranslation if key.startswith(temp)]
            if len(possibilities) == 0:
                reversedString = reversedString[1:]
                temp = ''
                continue
            
            if temp in possibilities:
                n2 = backwardTranslation[temp]
                break
            else:
                continue
    return int(n1+n2)

with open('input\\day1') as inputFile:
    rawData = [line.strip() for line in inputFile.readlines()]

#TASK 1
t1counter = 0
for line in rawData: t1counter += task1(line)
print(f'TASK 1: {t1counter}')

#TASK 2
t2counter = 0
for line in rawData: t2counter += task2(line)
print(f'TASK 2: {t2counter}')