
def off_by_one(line, next_line):
    diff_letters = {}
    for idx, (a, b) in enumerate(zip(line, next_line)):
        if a == b:
            continue
        else:
            diff_letters[a] = idx

    return len(diff_letters) == 1


with open('day-2-input') as f:

    data = f.readlines()
    for idx, line in enumerate(data):
        for next_line in data[idx:]:
            if off_by_one(line, next_line):
                a = line
                b = next_line
                break


def common_letters(line, next_line):
    # Make a string from the characters that are in both strings
    return ''.join([c for (c, d) in zip(line, next_line) if c == d])


print(f'The lines we are searching for are {a} & {b}')
print(f'The common letters are: \n {common_letters(a, b)}')
