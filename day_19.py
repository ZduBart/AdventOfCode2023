flows, parts = open("day_19_input.txt").read().split("\n\n")

A_ = lambda: 1 + x + m + a + s
R_ = lambda: 1
S_ = 0

exec(
    flows.replace(":", " and ")
    .replace(",", "_() or ")
    .replace("{", "_ = lambda: ")
    .replace("}", "_()")
)

exec(parts.replace(",", ";").replace("{", "").replace("}", ";S_+=in_()-1"))

print(S_)
