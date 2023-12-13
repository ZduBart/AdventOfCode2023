import re

with open('day_2_input.txt', 'r') as file:
    game_id_sum = 0
    for game in file:
        match = re.search(r'Game (\d+):', game)
        game_number = int(match.group(1))
        games = game.split(';')
        print(games)
        color_counts = {
            'red': [],
            'blue': [],
            'green': []
        }

        for single_game in games:
            counts = re.findall(r'(\d+)\s+(\w+)', single_game)
            for count, color in counts:
                color_counts[color].append(int(count))
        max_counts = {
            'red': max(color_counts['red']),
            'blue': max(color_counts['blue']),
            'green': max(color_counts['green'])
        }
        if max_counts['red'] <= 12 and max_counts['green'] <= 13 and max_counts['blue'] <= 14:
            game_id_sum += game_number
        print(max_counts)
    print(game_id_sum)