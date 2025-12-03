
part1, part2 = 0,0

with open("input.txt") as file:
    for line in file:

        line = line.replace("\n","")
        line = line[::-1]

        maxValue = 0
        secondValue = 0

        for i in range(0, len(line)):
            currentValue = int(line[i])
            if currentValue >= maxValue:
                if i == 0:
                    secondValue = currentValue
                else:
                    if maxValue >= secondValue:
                        secondValue = maxValue
                    maxValue = currentValue
        part1 += int(str(maxValue) + str(secondValue))

        part2Output = []

        for i in range(12, 0, -1):

            largestValue = 0
            valueIndex = 0

            for j in range(i - 1, len(line)):
                if int(line[j]) >= largestValue:
                    largestValue = int(line[j])
                    valueIndex = len(line) - j - 1

            line = line[::-1]
            lin = [ch for ch in line]

            while valueIndex >= 0:
                lin.pop(0)
                valueIndex -= 1

            part2Output += str(largestValue)
            line = "".join(lin)[::-1]

        part2 += int("".join(part2Output))
        print("".join(part2Output))

print(part1, part2)