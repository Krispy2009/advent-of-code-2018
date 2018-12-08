

def will_react(a, b):
    if a == b:
        return False
    return (a.upper() == b) or (a.lower() == b)


def react(data):
    idx = 0
    while idx < len(data):

        if idx < len(data)-1:
            if will_react(data[idx], data[idx+1]):
                data = data[:idx] + data[idx+2:]
                if idx > 2:
                    idx -= 2
                else:
                    idx = -1
        idx += 1
    return data


if __name__ == '__main__':

    with open('day-5-input') as f:
        data = f.readline().rstrip()

    data = react(data)

    print(f'We have {len(data)} chars left after we react')
