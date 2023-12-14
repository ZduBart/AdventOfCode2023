cards = list(open("day_4_input.txt"))
multiplier = [1 for _ in cards]
count = 0

for i, card in enumerate(cards):
    winning_numbers, my_numbers = card.split("|")
    winning_numbers = set(
        int(x) for x in winning_numbers.strip().split() if x.isdigit()
    )
    my_numbers = set(int(x) for x in my_numbers.strip().split() if x.isdigit())

    wins = winning_numbers.intersection(my_numbers)

    cmultiplier = multiplier[i]
    for j in range(i + 1, min(i + len(wins) + 1, len(cards))):
        multiplier[j] += cmultiplier

    count += cmultiplier

print(count)
