
part1, part2, = 0,0

paperMap = []

def isPaper(paper):
    if paper == "@" or paper == "X":
        return 1
    else:
        return 0

with open("input.txt") as file:
    for line in file:
        paperMap.append([ch for ch in line.replace("\n", "")])



    for x in range(len(paperMap)):
        for y in range(len(paperMap[x])):
            numAdjacent = 0

            if paperMap[x][y] == ".":
                continue

            if x > 0:
                numAdjacent = isPaper(paperMap[x - 1][y])
                if y > 0:
                    numAdjacent += isPaper(paperMap[x - 1][y - 1])
                if y < len(paperMap[x]) - 1:
                    numAdjacent += isPaper(paperMap[x - 1][y + 1])

            if x < len(paperMap) - 1:
                numAdjacent += isPaper(paperMap[x + 1][y])
                if y > 0:
                    numAdjacent += isPaper(paperMap[x + 1][y - 1])
                if y < len(paperMap[x]) - 1:
                    numAdjacent += isPaper(paperMap[x + 1][y + 1])

            if y > 0:
                numAdjacent += isPaper(paperMap[x][y - 1])
            if y < len(paperMap[x]) - 1:
                numAdjacent += isPaper(paperMap[x][y + 1])

            if numAdjacent < 4:
                part1 += 1


    addedInRound = 0

    while True:
        for x in range(len(paperMap)):
            for y in range(len(paperMap[x])):
                numAdjacent = 0

                if paperMap[x][y] == ".":
                    continue

                if x > 0:
                    numAdjacent = isPaper(paperMap[x - 1][y])
                    if y > 0:
                        numAdjacent += isPaper(paperMap[x - 1][y - 1])
                    if y < len(paperMap[x]) - 1:
                        numAdjacent += isPaper(paperMap[x - 1][y + 1])

                if x < len(paperMap) - 1:
                    numAdjacent += isPaper(paperMap[x + 1][y])
                    if y > 0:
                        numAdjacent += isPaper(paperMap[x + 1][y - 1])
                    if y < len(paperMap[x]) - 1:
                        numAdjacent += isPaper(paperMap[x + 1][y + 1])

                if y > 0:
                    numAdjacent += isPaper(paperMap[x][y - 1])
                if y < len(paperMap[x]) - 1:
                    numAdjacent += isPaper(paperMap[x][y + 1])

                if numAdjacent < 4:
                    addedInRound += 1
                    paperMap[x][y] = "X"

        part2 += addedInRound

        if addedInRound == 0:
            break

        addedInRound = 0

        for x in range(len(paperMap)):
            for y in range(len(paperMap[x])):
                if paperMap[x][y] == "X":
                    paperMap[x][y] = "."

    print(paperMap)

print(part1, part2)