xs, ys = zip(
    *[
        (x, y)
        for y, r in enumerate(open("day_11_input.txt"))
        for x, c in enumerate(r)
        if c == "#"
    ]
)


def dist(ps):
    ps = [sum((l, 1)[p in ps] for p in range(p)) for p in ps]
    return sum(abs(a - b) for a in ps for b in ps) // 2


for l in 2, 1000000:
    print(sum(map(dist, [xs, ys])))
