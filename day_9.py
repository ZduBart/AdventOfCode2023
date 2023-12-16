raports = open("day_9_input.txt").read().split("\n")

result = 0
for raport in raports:
    raport = raport.split(" ")
    raport = [int(i) for i in raport]
    next_row = raport
    single_raport = []
    single_raport.append(raport)
    while not all(x == 0 for x in next_row):
        next_row = [
            int(next_row[i + 1] - next_row[i]) for i in range(0, len(next_row) - 1)
        ]
        single_raport.append(next_row)
        print(next_row)

    next_value = 0
    for n in single_raport[::-1]:
        print(n)
        next_value = n[0] - next_value
        print(next_value)
    result += next_value

print(result)
