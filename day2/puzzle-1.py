
def check_line(line):
    counts = {}
    for ch in line:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    has_two = int(2 in counts.values())
    has_three = int(3 in counts.values())
    return has_two, has_three


with open('day-2-input') as f:
    counts = [0, 0]
    data = f.readlines()
    for line in data:
        has_two, has_three = check_line(line)
        counts[0] += has_two
        counts[1] += has_three

print(f'My checksum is: {counts[0] * counts[1]}')
