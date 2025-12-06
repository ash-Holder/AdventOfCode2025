
part1, part2 = 0,0

freshIDS = []
usedIDS = []

with open("input.txt") as file:
    for line in file:
        print(line)
        if "-" in line:
            freshIDS.append([int(line.split("-")[0]), int(line.split("-")[1])])
        else:
            id = int(line.replace("\n", ""))
            for x in freshIDS:
                if x[0] <= id and id <= x[1]:
                    part1 += 1
                    break

    freshIDS = sorted(freshIDS, key=lambda x: x[0])

    print(freshIDS)

    for x in freshIDS:
        if usedIDS == []:
            usedIDS.append(x)
        else:
            for y in usedIDS:
                if x[0] <= y[0] and x[1] >= y[1]:
                    usedIDS.remove(y)
                elif x[0] <= y[0] <= x[1] <= y[1]:
                    x[1] = y[1]
                    usedIDS.remove(y)
                elif y[0] <= x[0] <= y[1] <= x[1]:
                    x[0] = y[0]
                    usedIDS.remove(y)
                elif x[0] >= y[0] and x[1] <= y[1]:
                     break

        overLap = 0
        for y in usedIDS:
            if x[0] >= y[0] and x[1] <= y[1]:
                overLap += 1
        if overLap == 0:
            usedIDS.append(x)

    print(usedIDS)

    used = []

    for x in usedIDS:
        if x not in used:
            part2 += x[1] - x[0] + 1
            used.append(x)


print(part1, part2)