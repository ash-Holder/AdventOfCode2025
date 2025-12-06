
part1, part2 = 0,0

digits = []
operations = []

chars = []

with open("input.txt") as f:
    for line in f:
        if "*" in line:
            operations = line.split()
        else:
            digits.append([int(x) for x in line.split()])

            characters = [ch for ch in line.replace("\n", "")]
            chars.append(characters)

    print(digits)
    print(operations)
    print(chars)

    for i in range(len(operations)):
        operator = operations[i]

        result = 0

        for j in range(len(digits)):
            if operator == '*':
                if result == 0:
                    result = 1
                result *= digits[j][i]
            else:
                result += digits[j][i]

        part1 += result

    i = 0
    currentOp = 0

    currentDigits = []

    currentChar = chars[0][i]
    nextChar = chars[0][i + 1]

    while currentChar != ' ' and nextChar != ' ' and i < len(chars[0]):
        currentDigits.append("".join(chars[0][i] + chars[1][i] + chars[2][i] + chars[3][i]))
        i += 1
        #print(currentDigits)

    i = 0
    j = 0

    currentSubtotal = 0

    while True:

        if i >= len(operations) or j >= len(currentDigits):
            break

        print(currentDigits[j], j)

        currentOperator = operations[i]

        if currentDigits[j] == ' ' or currentDigits[j] == '  ' or currentDigits[j] == '   ' or currentDigits[j] == '    ':
            part2 += currentSubtotal
            currentSubtotal = 0
            i = i + 1
            j = j + 1
            continue

        if currentOperator == '+':
            part2 += int(currentDigits[j])
        else:
            if currentSubtotal == 0:
                currentSubtotal = 1
            currentSubtotal = currentSubtotal * int(currentDigits[j])

        j += 1

print(part1, part2)
