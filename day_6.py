file = open("day_6_input.txt").read().split("\n")
times = [int(n) for n in file[0].split(" ") if n.isdigit()]
record_dist = [int(n) for n in file[1].split(" ") if n.isdigit()]
races = list(zip(times, record_dist))


def calculate(races):
    result = 1
    for race in races:
        ways_to_win = 0
        for i in range(1, race[0]):
            time_left = race[0] - i
            distance_traveled = i * time_left
            if distance_traveled > race[1]:
                ways_to_win += 1
        result *= ways_to_win
    return result
