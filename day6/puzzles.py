import sys
from collections import Counter


data = []
with open('day-6-input') as f:
    biggest = 0
    for line in f.readlines():
        row = tuple(int(i) for i in line.rstrip().split(','))
        data.append(row)
        if row[0] > biggest:
            biggest = row[0]
        elif row[1] > biggest:
            biggest = row[1]
    biggest += 1

PLAIN = [[None for i in range(biggest)] for j in range(biggest)]
DISTANCES = [[sys.maxsize for i in range(biggest)] for j in range(biggest)]


def manhattan_distance(points):
    distance = 0
    for a, b in points:
        distance += abs(a - b)
    return distance


def find_shelter_from_danger():
    for idx, line in enumerate(data):
        # for every point in our supplied coordinates
        # set it's name to be the idx
        x, y = int(line[0]), int(line[1])
        PLAIN[y][x] = idx
        # a point has distance 0 from itself
        DISTANCES[x][y] = 0
        for i, row in enumerate(DISTANCES):
            for j, curr_distance in enumerate(row):
                # for every point in our PLAIN, calculate a distance between
                # the coordinates (x,y) we are checking at the moment and the
                # current point (i,j)

                distance = manhattan_distance(((x, i), (y, j)))

                if (curr_distance >= distance):
                    # If we are here, we have found a smaller distance
                    # e.g a closer point
                    # save it in our DISTANCES map
                    if distance and DISTANCES[i][j] == distance:
                        PLAIN[j][i] = '.'
                    else:
                        # mark this point as the closest point to the coordinates (x,y)
                        # and note it's distance in the DISTANCES list
                        DISTANCES[i][j] = distance
                        PLAIN[j][i] = idx


def find_safe_areas():
    for i, row in enumerate(PLAIN):
        for j, point in enumerate(row):
            for x, y in data:
                distance = manhattan_distance(((x, i), (y, j)))
                DISTANCES[i][j] += distance


def infinity_filters():
    # Check the outer layer of the plain and mark all points as infinite
    # since whatever is on the edge will continue outwards

    infinite_idxs = set()
    for a, row in enumerate(PLAIN):
        for b, element in enumerate(row):
            if a in(0, len(PLAIN)-1) or b in (0, len(row)-1):
                infinite_idxs.add(element)

    return infinite_idxs


if __name__ == '__main__':

    print('PUZZLE 1 \n---------')
    PLAIN = [[None for i in range(biggest)] for j in range(biggest)]
    DISTANCES = [[sys.maxsize for i in range(biggest)] for j in range(biggest)]

    find_shelter_from_danger()

    flat_PLAIN = [i for sublist in PLAIN for i in sublist]

    counts = Counter(flat_PLAIN)

    infinite_idx = infinity_filters()
    # keep the counts for finite areas
    for idx in infinite_idx:
        counts.pop(idx)
    from operator import itemgetter
    area  = sorted(counts.items(), key=itemgetter(1), reverse=True)[0][1]
    print(f'Area of least dangerous place: {area}')

    # Part2
    print('\nPUZZLE 2 \n---------')

    PLAIN = [[None for i in range(biggest)] for j in range(biggest)]
    DISTANCES = [[0 for i in range(biggest)] for j in range(biggest)]

    find_safe_areas()

    flat_distances = [i for sublist in DISTANCES for i in sublist]

    ans = [i for i in flat_distances if i < 10000]
    print(f'Area of safe place: {len(ans)}')
