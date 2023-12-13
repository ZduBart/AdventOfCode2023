with open('day_1_input.txt', 'r') as file:
    control_sum = 0
    for line in file:
        first_number = None
        last_number = None
        for letter in line:
            if letter.isdigit() and first_number is None:
                first_number = letter
                last_number = letter
            elif letter.isdigit() and first_number is not None:
                last_number = letter
        control_sum += int(first_number + last_number)


print(control_sum)
