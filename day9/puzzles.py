

def pretty_print(circle, idx):
    marked = [f'({m})' if i == idx else f'{m}' for i, m in enumerate(circle)]
    pretty = '  '.join(marked)
    return pretty


def play(num_players, marbles):

    marbles = list(range(marbles+1))
    current_marble_idx = 0
    players = [0] * num_players
    circle = [marbles.pop(0)]
    # print(f'[-]', pretty_print(circle, current_marble_idx))

    # import pudb; pu.db
    while marbles:
        for player in range(num_players):
            if marbles:
                current_marble = marbles.pop(0)
                # current_marble_idx = 1
                if current_marble % 23 == 0:
                    players[player] += current_marble
                    players[player] += circle.pop(current_marble_idx - 6)
                    current_marble_idx = current_marble_idx - 7
                    current_marble = circle[current_marble_idx]
                else:
                    if current_marble == 1:
                        circle.append(current_marble)
                        current_marble_idx = 1
                    else:
                        insert_idx = ((current_marble_idx+2) % (len(circle)))
                        circle.insert(insert_idx+1, current_marble)
                        current_marble_idx = insert_idx
                # print(f'[{player+1}]',pretty_print(circle, current_marble_idx))
            else:
                print(max(players))
                break

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
    """

    # play(9, 25)
    # play(10, 1618)
    # play(13, 7999)
    # play(17, 1104)
    # play(21, 6111)
    # play(30, 5807)
    play(464, 71730)
