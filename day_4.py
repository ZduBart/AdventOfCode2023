cards = list(open("day_4_input.txt"))
score = 0
for card in cards:
    winning_numbers = [int(c) for c in card.split("|")[0].split(" ") if c.isdigit()]
    my_numbers = [int(c) for c in card.split("|")[1].strip().split(" ") if c.isdigit()]
    power = 0
    for n in my_numbers:
        if n in winning_numbers:
            power += 1
    if power:
        score += 2 ** (power - 1)
print(score)
