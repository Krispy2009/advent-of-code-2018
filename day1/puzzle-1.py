def get_data():
    values = []
    with open('puzzle-input', 'r') as f:
        data = f.readlines()
        for line in data:
            values.append(int(line))

    return values


data = get_data()
print(sum(data))
