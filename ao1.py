import math

dial = 50

result = 0

with open("input.txt") as file:
    for line in file:
        dir = line[0]
        value = int(line[1:])

        if dir == 'R':
            for i in range(value):
                dial = (dial + 1) % 100
                result += dial == 0
        if dir == 'L':
            for i in range(value):
                dial = (dial - 1) % 100
                result += dial == 0

        print(dial, result)




print(result)