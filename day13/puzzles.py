
with open('small') as f:
    data = f.readlines()
    data = [d.replace('\n', '') for d in data]


class Cart:
    def __init__(self, y, x, direction):
        self.y = y
        self.x = x
        self.direction = direction
        self.intersections = 0
        self.crashed = False

    def move(self, track_ahead):
        if track_ahead in 'v^><':
            self.direction = 'X'
            self.crashed = True
        if track_ahead == '|':
            if self.direction == '^':
                self.y -= 1
            elif self.direction == 'v':
                self.y += 1

        if track_ahead == '-':
            if self.direction == '<':
                self.x -= 1
            elif self.direction == '>':
                self.x += 1

        if track_ahead == '/':
            if self.direction == 'v':
                self.y += 1
                self.direction = '<'
            if self.direction == '>':
                self.x += 1
                self.direction = '^'

        if track_ahead == '\\':
            if self.direction == 'v':
                self.y += 1
                self.direction = '>'
            if self.direction == '<':
                self.x -= 1
                self.direction = '^'

        if track_ahead == '+':
            if self.direction == 'v':
                self.y += 1
            elif self.direction == '^':
                self.y -= 1
            elif self.direction == '>':
                self.x += 1
            elif self.direction == '<':
                self.x -= 1
        self.direction = self.turn_at_intersection()

    def turn_at_intersection(self):
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

print(carts)


def find_next_track(x, y, direction):
    if direction == '^':
        next_track = data[y-1][x]
        curr_track = '|'
    elif direction == 'v':
        next_track = data[y+1][x]
        curr_track = '|'
    elif direction == '<':
        next_track = data[x-1][x]
        curr_track = '-'
    elif direction == '>':
        next_track = data[x+1][x]
        curr_track = '-'

    return next_track, curr_track

def pretty_print(data):
    for row in data:
        print(row)

while True:
    for idx, row in enumerate(data):
        import pdb; pdb.set_trace()
        for idx2, column in enumerate(row):
            if column in '<>^v':
                curr_cart = None
                for cart in carts:
                    if cart.y == idx and cart.x == idx2:
                        curr_cart = cart
                        break
                next_track, curr_track = find_next_track(idx2, idx, data[idx][idx2])
                curr_cart.move(next_track)
                data[idx].replace(column, curr_track)
                data[curr_cart.y].replace(data[curr_cart.y][curr_cart.x], curr_cart.direction)

                if curr_cart.crashed:
                    sys.exit(0)

    pretty_print(data)
