def get_data():
    values = []
    with open('puzzle-input', 'r') as f:
        data = f.readlines()
        for line in data:
            values.append(int(line))

    return values


data = get_data()
reached = False
result = 0
frequencies = set({0})
while not reached:
    for d in data:
        result += d
        if result in frequencies:
            print(f'{result} already reached')
            reached = True
            break
        frequencies.add(result)
