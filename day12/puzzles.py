DIFF_IN_SUM = 0
SUM = 0
PREV_SUM = 0

with open('day-12-input') as f:
    initial = f.readline().rstrip().split(':')[1].replace(' ', '')
    data = f.readlines()

    data = [item.rstrip() for item in data if item.rstrip()]

instructions = [instruction.split(' => ') for instruction in data]
instructions = {instruction[0]: instruction[1] for instruction in instructions}

DIFF_IN_SUM = 0
PREV_SUM = 0


def calc_generation(current, instructions):
    global PREV_SUM
    global DIFF_IN_SUM
    current_copy = list(current[:])
    for i in range(1, 161):
        for idx, area in enumerate(range(4, len(current)-4)):
            if current[area:area+5] in instructions:
                current_copy[idx+6] = instructions[current[area:area+5]]
            else:
                current_copy[idx+6] = '.'
        current = ''.join(current_copy)

        sum = 0
        for x in range(-20, len(current)-20):
            if current[x+20] == '#':
                sum += x
        DIFF_IN_SUM = (sum - PREV_SUM)
        PREV_SUM = sum
        print(f'{i}: {current}   ---   {DIFF_IN_SUM}')

    # Calculate 50 billionth generation
    # Anything over 160 generations increases the sum by 33 so
    # sum up to 160 + (50000000000 - 160)*33 = ans

    if i == 160:
        other_gens = (50000000000 - 160)*33
        print(f'Sum at 50 billionth generation:  {sum+other_gens}')


if __name__ == '__main__':
    initial = '.'*20 + initial + '.'*500
    print('0:', initial)
    calc_generation(initial, instructions)
