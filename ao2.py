

result = 0

def idChecker(id):

    s = str(id)
    length = len(s)
    for patLength in range(1, length // 2 + 1):
        #print(patLength)
        if length % patLength != 0:
            continue

        pattern = s[:patLength]
        #print(pattern)
        if pattern * (length // patLength) == s:
            print(id)
            return id

    return 0





with open("input.txt") as file:
    content = file.read().replace('\n', '').split(",")
    for x in content:
        ids = x.split("-")
        ids = [int(x) for x in ids]
        for i in range(ids[0], ids[1] + 1):
            result += idChecker(i)
            # print(result)
print(result)