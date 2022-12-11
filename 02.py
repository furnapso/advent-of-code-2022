def main():
    with open("02_input.txt") as f:
        input = f.read().strip()

    input_data = input.split("\n")

    score = 0

    for i in input_data:
        vals = i.split(" ")
        score += calculate_score(vals[0], vals[1])

    print(f"Part one: {score}")

    score = 0

    for i in input_data:
        vals = i.split(" ")
        vals[1] = get_move(vals[0], vals[1])
        score += calculate_score(vals[0], vals[1])

    print(f"Part two: {score}")


def calculate_score(player1: str, player2: str) -> int:
    player1_map = {
        'A': 'ROCK',
        'B': 'PAPER',
        'C': 'SCISSORS'
    }

    player2_map = {
        'X': 'ROCK',
        'Y': 'PAPER',
        'Z': 'SCISSORS'
    }

    selection_score_map = {
        'ROCK': 1,
        'PAPER': 2,
        'SCISSORS': 3
    }

    player1_decoded = player1_map[player1]
    player2_decoded = player2_map[player2]

    score = selection_score_map[player2_decoded]

    if player2_decoded == 'ROCK' and player1_decoded == 'SCISSORS':
        score += 6
    elif player2_decoded == 'PAPER' and player1_decoded == 'ROCK':
        score += 6
    elif player2_decoded == 'SCISSORS' and player1_decoded == 'PAPER':
        score += 6
    elif player2_decoded == player1_decoded:
        score += 3

    return score


def get_move(player1: str, outcome: str):
    player1_map = {
        'A': 'ROCK',
        'B': 'PAPER',
        'C': 'SCISSORS'
    }

    move_map = {
        'ROCK': 'X',
        'PAPER': 'Y',
        'SCISSORS': 'Z'
    }

    outcome_map = {
        'X': 'LOSE',
        'Y': 'DRAW',
        'Z': 'WIN'
    }

    outcome_decoded = outcome_map[outcome]
    player1_decoded = player1_map[player1]

    if outcome_decoded == 'DRAW':
        return move_map[player1_decoded]

    elif outcome_decoded == 'WIN':
        if player1_decoded == 'ROCK':
            return move_map['PAPER']
        elif player1_decoded == 'PAPER':
            return move_map['SCISSORS']
        elif player1_decoded == 'SCISSORS':
            return move_map['ROCK']

    elif outcome_decoded == 'LOSE':
        if player1_decoded == 'ROCK':
            return move_map['SCISSORS']
        elif player1_decoded == 'PAPER':
            return move_map['ROCK']
        elif player1_decoded == 'SCISSORS':
            return move_map['PAPER']


if __name__ == "__main__":
    main()
