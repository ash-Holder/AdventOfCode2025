import functools


part1, part2 = 0,0

characters = []
startPoint = 0

@functools.lru_cache(maxsize=100000)
def recursiveTeleport(column, row):
    if column >= len(characters) - 1:
        return 0

    if characters[column+1][row] == '^':
        characters[column + 1][row-1] = '|'
        characters[column + 1][row+1] = '|'
        leftSplits = recursiveTeleport(column + 1, row - 1)
        rightSplits = recursiveTeleport(column + 1, row + 1)
        return 1 + leftSplits + rightSplits
    else:
        characters[column + 1][row] = '|'
        return recursiveTeleport(column + 1, row)


with open("input.txt") as file:
    for line in file:
        characters.append([ch for ch in line.replace("\n", "")])
        if 'S' in line:
            startPoint = characters[0].index("S")

    part2 = recursiveTeleport(0, startPoint) + 1
    for i in range(len(characters)):
        for j in range(len(characters[i])):
            if characters[i][j] == '^' and characters[i-1][j] == '|':
                part1 += 1



print(part1, part2)


