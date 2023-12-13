import re

with open("day_2_input.txt", "r") as file:
    game_sum = 0
    for game in file:
        match = re.search(r"Game (\d+):", game)
        game_number = int(match.group(1))
        games = game.split(";")
        print(games)
        color_counts = {"red": [], "blue": [], "green": []}

        for single_game in games:
            counts = re.findall(r"(\d+)\s+(\w+)", single_game)
            for count, color in counts:
                color_counts[color].append(int(count))
        max_counts = {
            "red": max(color_counts["red"]),
            "blue": max(color_counts["blue"]),
            "green": max(color_counts["green"]),
        }
        game_sum += max_counts["red"] * max_counts["green"] * max_counts["blue"]
        print(max_counts)
    print(game_sum)
