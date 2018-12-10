import re
import copy
import time
with open('day-10-input') as f:
    data = f.readlines()

PLAIN = [['.'] * 150 for i in range(150)]
RE = re.compile(r'-?\d+')
points = []

for line in data:
    x, y, vx, vy = re.findall(RE, line)
    points.append([int(x), int(y), int(vx), int(vy)])


def apply_velocities(points):
    for idx, (x, y, vx, vy) in enumerate(points):
        points[idx][0] += vx
        points[idx][1] += vy
    return points


def pretty_print(points):
    plain = copy.deepcopy(PLAIN)

    for x, y, vx, vy in points:
        if y < 150 and x < 250 and y > 0 and x > 100:
            plain[y][x-100] = '#'

    out = ''
    for line in plain:
        out += ''.join(line) + '\n'
    print(f'{out}', end='\r', flush=True)
    print()


for i in range(10900):
    points = apply_velocities(points)
    if i > 10870:
        pretty_print(points)
        print(i)
        time.sleep(0.2)
