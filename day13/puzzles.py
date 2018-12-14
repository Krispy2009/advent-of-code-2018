import sys
import copy
from operator import attrgetter

with open('day-13-input') as f:
    data = f.readlines()
    data = [d.replace('\n', '') for d in data]

og_track = copy.deepcopy(
    [
        l.replace('>', '-').replace('<', '-').replace('v', '|').replace('^', '|')
        for l in data
    ]
)

data = [list(l) for l in data]


class Cart:
    def __init__(self, y, x, direction):
        self.y = y
        self.x = x
        self.direction = direction
        self.prev_direction = None
        self.intersections = 0
        self.crashed = False
        self.has_moved = False

        if direction in '><':
            self.curr_track = '-'
        else:
            self.curr_track = '|'

    def move(self, track_ahead):

        self.prev_direction = self.direction

        if track_ahead in 'v^><':
            if self.direction == 'v':
                self.y += 1
            elif self.direction == '^':
                self.y -= 1
            elif self.direction == '>':
                self.x += 1
            else:
                self.x -= 1

            self.direction = data[self.y][self.x]
            self.crashed = True
            print(f'CRASHHHHH {self.x},{self.y}')
            data[self.y][self.x] = og_track[self.y][self.x]
            other_cart = [
                cart for cart in carts
                if (cart.x == self.x and cart.y == self.y and not cart.crashed)
            ][0]

            other_cart.crashed = True
            self.curr_track = og_track[self.y][self.x]
            data[other_cart.y][other_cart.x] = og_track[other_cart.y][other_cart.x]
            self.direction = self.curr_track

        elif track_ahead == '|':
            if self.direction == '^':
                self.y -= 1
            elif self.direction == 'v':
                self.y += 1

        elif track_ahead == '-':
            if self.direction == '<':
                self.x -= 1
            elif self.direction == '>':
                self.x += 1

        elif track_ahead == '/':
            if self.direction == 'v':
                self.y += 1
                self.direction = '<'
            elif self.direction == '>':
                self.x += 1
                self.direction = '^'
            elif self.direction == '<':
                self.x -= 1
                self.direction = 'v'
            elif self.direction == '^':
                self.y -= 1
                self.direction = '>'

        elif track_ahead == '\\':
            if self.direction == 'v':
                self.y += 1
                self.direction = '>'
            elif self.direction == '<':
                self.x -= 1
                self.direction = '^'
            elif self.direction == '^':
                self.y -= 1
                self.direction = '<'
            elif self.direction == '>':
                self.x += 1
                self.direction = 'v'

        elif track_ahead == '+':
            if self.direction == 'v':
                self.y += 1
            elif self.direction == '^':
                self.y -= 1
            elif self.direction == '>':
                self.x += 1
            elif self.direction == '<':
                self.x -= 1
            self.direction = self.turn_at_intersection()
            self.intersections += 1
        self.curr_track = og_track[self.y][self.x]
        self.has_moved = True

    def turn_at_intersection(self):
        # print(f'This is intersection no: {self.intersections} for {self.id}')
        dirs = {
            '<': 'v<^',
            '^': '<^>',
            '>': '^>v',
            'v': '>v<',
        }
        return dirs[self.direction][self.intersections % 3]


carts = []

for idx, row in enumerate(data):
    for idx2, column in enumerate(row):
        if column in '<>^v':
            carts.append(Cart(idx, idx2, column))


def pretty_print(data):
    for row in data:
        print(''.join(row))


def find_next_track(x, y, direction):

    if direction == '^':
        next_track = data[y-1][x]

    elif direction == 'v':
        next_track = data[y+1][x]

    elif direction == '<':
        next_track = data[y][x-1]

    elif direction == '>':
        next_track = data[y][x+1]

    return next_track


while len(carts) > 1:
    for cart in sorted(carts, key=attrgetter('y', 'x')):
        if not cart.crashed:
            x, y = cart.x, cart.y
            track_ahead = find_next_track(x, y, cart.direction)
            cart.move(track_ahead)
            data[cart.y][cart.x] = cart.direction
            data[y][x] = og_track[y][x]

    cartos = [cart for cart in carts if not cart.crashed]
    if len(cartos) == 1:
        print(cartos[0].x, cartos[0].y)
        sys.exit(0)
