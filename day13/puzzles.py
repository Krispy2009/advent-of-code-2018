import time
import sys
import copy
#with open('small2') as f:
with open('day-13-input') as f:
    data = f.readlines()
    data = [d.replace('\n', '') for d in data]

original_track = copy.deepcopy(
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
        self.just_passed_intersection = False
        self.intersections = 0
        self.crashed = False
        self.has_moved = False

        if direction in '><':
            self.curr_track = '-'
        else:
            self.curr_track = '|'

    def move(self, track_ahead):

        self.prev_direction = self.direction
        self.just_passed_intersection = False

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
            other_cart = [
                cart for cart in carts
                if (cart.x == self.x and cart.y == self.y and not cart.crashed)
            ][0]

            other_cart.crashed = True
            self.curr_track = original_track[self.y][self.x]
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
            self.just_passed_intersection = True
            self.intersections += 1
        self.curr_track = original_track[self.y][self.x]
        self.has_moved = True

    def turn_at_intersection(self):
        # print(f'This is intersection no: {self.intersections} for {self.id}')
        dirs = {
            '<': 'v<^',
            '^': '<^>',
            '>': '^>v',
            'v': '>v<',
        }
        try:
            return dirs[self.direction][self.intersections % 3]
        except KeyError:
            import pdb; pdb.set_trace()


carts = []


for idx, row in enumerate(data):
    for idx2, column in enumerate(row):
        if column in '<>^v':
            carts.append(Cart(idx, idx2, column))


def pretty_print(data):
    for row in data:
        print(''.join(row))


pretty_print(original_track)
sys.exit(0)


def find_next_track(x, y, direction, cart):
    prev_direction = cart.prev_direction

    if direction == '^':
        next_track = data[y-1][x]
        if prev_direction == '<':
            curr_track = '\\'
        elif prev_direction == '>':
            curr_track = '/'
        else:
            curr_track = '|'

    elif direction == 'v':
        next_track = data[y+1][x]
        if prev_direction == '>':
            curr_track = '\\'
        elif prev_direction == '<':
            curr_track = '/'
        else:
            curr_track = '|'

    elif direction == '<':
        next_track = data[y][x-1]
        if prev_direction == '^':
            curr_track = '\\'
        elif prev_direction == 'v':
            curr_track = '/'
        else:
            curr_track = '-'
    elif direction == '>':
        next_track = data[y][x+1]
        if prev_direction == '^':
            curr_track = '/'
        elif prev_direction == 'v':
            curr_track = '\\'
        else:
            curr_track = '-'

    if cart.just_passed_intersection:
        curr_track = '+'

    return next_track, curr_track


while True:
    idx = 0
    while idx < len(data):
        idx2 = 0
        while idx2 < len(data[idx]):
            if data[idx][idx2] in '<>^v':
                curr_cart = None
                for cart in carts:
                    if cart.y == idx and cart.x == idx2:
                        curr_cart = cart
                        break
                if not curr_cart.has_moved and not curr_cart.crashed:
                    next_track, curr_track = find_next_track(
                        idx2, idx,
                        data[idx][idx2], curr_cart
                    )

                    curr_cart.move(next_track)
                    # print(
                    #    f' Moved ({idx2},{idx}) -> '
                    #    f'({curr_cart.x},{curr_cart.y}) new dir {curr_cart.direction}'
                    # )
                    data[idx][idx2] = original_track[idx][idx2]
                    data[curr_cart.y][curr_cart.x] = curr_cart.direction
                    if data[idx][idx2] == 'X':
                        data[idx][idx2] = original_track[idx][idx2]
                    idx2 += 1

                remaining_carts = [cart for cart in carts if not cart.crashed]
                #print(f'remaining: {len(remaining_carts)}')
                if len(remaining_carts) == 1:
                    cart = remaining_carts[0]

                    if cart.direction == 'v':
                        cart.y += 1
                    if cart.direction == '^':
                        cart.y -= 1

                    if cart.direction == '>':
                        cart.x += 1
                    if cart.direction == '<':
                        cart.x -= 1

                    #pretty_print(data)

                    print(f'Last one standing: ({cart.x},{cart.y})')
                    sys.exit(0)
                # part 1
                # if curr_cart.crashed:
                #     pretty_print(data)
                #     sys.exit(0)
            #print(idx, idx2, '---> ', len([cart for cart in carts if not cart.crashed]))
            # if len([cart for cart in carts if not cart.crashed]) == 3 and idx == 123 and idx2 == 36:
            #     import pdb; pdb.set_trace()
            idx2 += 1
        idx += 1
    for cart in carts:
        cart.has_moved = False

    pretty_print(data)
    #time.sleep(0.5)
