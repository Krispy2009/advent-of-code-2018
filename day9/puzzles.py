from blist import blist


def pretty_print(circle, idx):
    marked = [f'({m})' if i == idx else f'{m}' for i, m in enumerate(circle)]
    pretty = '  '.join(marked)
    return pretty


def play(num_players, num_marbles):
    current_marble_idx = 0
    players = [0] * num_players
    circle = blist([0])
    print(f'[-]', pretty_print(circle, current_marble_idx))
    current_marble = 1
    while True:
        player = 0
        while player < num_players:

            if current_marble % 23 == 0:
                players[player] += current_marble
                current_marble_idx = current_marble_idx - 7
                if current_marble_idx < 0:
                    current_marble_idx += len(circle)
                players[player] += circle.pop(current_marble_idx)

            else:
                if current_marble == 1:
                    circle.append(current_marble)
                    current_marble_idx = 1
                else:
                    insert_idx = ((current_marble_idx+2) % (len(circle)))
                    if insert_idx == 0:
                        insert_idx = len(circle)
                    circle.insert(insert_idx, current_marble)
                    current_marble_idx = insert_idx
            current_marble += 1

            player += 1
            #print(f'[{player}]', pretty_print(circle, current_marble_idx))

            if current_marble > num_marbles:
                print(f'{num_players} - {num_marbles} --> {max(players)}')
                return


if __name__ == '__main__':
    """
    examples:
    9 players; last marble is worth 25 points; high score is 32
    10 players; last marble is worth 1618 points: high score is 8317
    13 players; last marble is worth 7999 points: high score is 146373
    17 players; last marble is worth 1104 points: high score is 2764
    21 players; last marble is worth 6111 points: high score is 54718
    30 players; last marble is worth 5807 points: high score is 37305

    challenge:
    464 players; last marble is worth 71730 points

    extra examples:
    9 players; last marble is worth 48 points: high score is 63
    1 players; last marble is worth 48 points: high score is 95

    """


    #play(9, 25) # 32
    #play(10, 1618) # 8317
    # play(13, 7999) # 146373
    # play(17, 1104) # 2764
    #play(21, 6111) # 54718
    # play(30, 5807) # 37305

    #Part 1
    # play(464, 71730) # 380705
    #Part 2
    play(464, 7173000) # 3175950420
