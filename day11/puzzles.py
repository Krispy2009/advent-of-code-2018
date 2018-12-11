from blist import blist

GRID = [[i+1 for i in range(300)] for j in range(300)]
SERIAL_ID = 9005


def make_power_levels(grid):
    for idx, row in enumerate(grid):
        for cell in row:
            rack_id = cell + 10
            power_level = rack_id * (idx + 1)
            power_level = power_level + SERIAL_ID
            power_level = power_level * rack_id
            power_level = find_hundreds(power_level)
            power_level -= 5
            grid[idx][cell-1] = power_level
    return grid


def find_hundreds(power_level):
    pl_str = str(power_level)
    if len(pl_str) > 2:
        hundreds_digit = pl_str[-3]
    else:
        hundreds_digit = 0

    return int(hundreds_digit)


def find_submatrix(grid, subgrid_len):
    i = 0
    j = 0
    solutions = blist()
    while i < len(grid) - subgrid_len:
        sol = blist()
        j = 0
        while j < len(grid) - subgrid_len:
            submatrix = [
                grid[x+i][y+j]
                for y in range(subgrid_len)
                for x in range(subgrid_len)
            ]
            sol.append(sum(submatrix))
            j += 1
        solutions.append(sol)
        i += 1

    # All the sums are there, now find the biggest one along with it's idx
    biggest = 0
    biggest_idx = 0
    for idx, a in enumerate(solutions):
        for idx2, b in enumerate(a):
            if biggest < b:
                biggest = b
                biggest_idx = (idx2+1, idx+1)

    print(biggest, biggest_idx, subgrid_len)


if __name__ == '__main__':
    grid = make_power_levels(GRID)
    for i in range(2, 300):
        find_submatrix(grid, i)