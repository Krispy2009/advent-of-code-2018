import re
RE = re.compile(r'#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<height>\d+)x(?P<width>\d+)')


def get_instructions():
    with open('day3-input', 'r') as f:
        instructions = f.readlines()

    return instructions


def make_claims(instructions):
    for instruction in instructions:
        x, y, width, height = parse_instruction(instruction)
        for p1 in range(x, x+width):
            for p2 in range(y, y+height):
                FABRIC[p2][p1] += 1




def parse_instruction(instruction):
    # format: #ID @ `x`,`y`: `width`x`height`
    i, x, y, w, h = re.match(RE, instruction).groups()
    INSTRUCTION_MANUAL[i] = (int(x), int(y), int(w), int(h))
    return INSTRUCTION_MANUAL[i]


def calculate_overlaps():
    # flatten list
    flat_list = [i for sublist in FABRIC for i in sublist if i > 1]
    print(f'Puzzle 1: Number of overlaps: {len(flat_list)}')


def find_intact():
    for i in INSTRUCTION_MANUAL:
        x, y, w, h = INSTRUCTION_MANUAL[i]
        submatrix = [row[x:x+w] for row in FABRIC[y:y+h]]
        flat_submatrix = [i for sublist in submatrix for i in sublist]

        if sum(flat_submatrix) == (w * h):
            print(f'Puzzle 2: Claim #{i} is intact')
            break


if __name__ == '__main__':

    INSTRUCTION_MANUAL = {}
    instructions = get_instructions()
    size = len(instructions)

    FABRIC = [[0 for x in range(size)] for y in range(size)]

    make_claims(instructions)

    # Puzzle 1
    calculate_overlaps()
    # Puzzle 2
    find_intact()
