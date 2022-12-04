INPUT_FILE_NAME: str = "input.txt"

class RockPaperScissorsGame:
    POINTS_PER_WIN = 6
    POINTS_PER_TIE = 3

    OPPONENT_ROCK = "A"
    OPPONENT_PAPER = "B"
    OPPONENT_SCISSORS = "C"

    MY_ROCK = "X"
    MY_PAPER = "Y"
    MY_SCISSORS = "Z"
    MY_SHAPE_SCORE = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    OPPONENT_MY_SHAPE_MAPPING = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }

    MY_LOSS = "X"
    MY_TIE = "Y"
    MY_WIN = "Z"

    def __init__(self, opponent_move: str, my_move: str):
        self.opponent_move = opponent_move
        self.my_move = my_move

    def is_my_win(self) -> bool:
        if self.opponent_move == self.OPPONENT_ROCK:
            return self.my_move == self.MY_PAPER
        elif self.opponent_move == self.OPPONENT_PAPER:
            return self.my_move == self.MY_SCISSORS
        elif self.opponent_move == self.OPPONENT_SCISSORS:
            return self.my_move == self.MY_ROCK
        else:
            return False

    def is_tie(self) -> bool:
        return self.OPPONENT_MY_SHAPE_MAPPING[self.opponent_move] == self.my_move

    def my_score_initial_interpretation(self) -> int:
        score = self.MY_SHAPE_SCORE[self.my_move]

        if self.is_my_win():
            score += self.POINTS_PER_WIN
        elif self.is_tie():
            score += self.POINTS_PER_TIE

        return score

    def my_score_final_interpretation(self) -> int:
        score = 0

        if self.my_move == self.MY_LOSS:
            if self.opponent_move == self.OPPONENT_ROCK:
                score += 3
            elif self.opponent_move == self.OPPONENT_PAPER:
                score += 1
            elif self.opponent_move == self.OPPONENT_SCISSORS:
                score += 2
        elif self.my_move == self.MY_TIE:
            score += self.POINTS_PER_TIE

            if self.opponent_move == self.OPPONENT_ROCK:
                score += 1
            elif self.opponent_move == self.OPPONENT_PAPER:
                score += 2
            elif self.opponent_move == self.OPPONENT_SCISSORS:
                score += 3
        elif self.my_move == self.MY_WIN:
            score += self.POINTS_PER_WIN

            if self.opponent_move == self.OPPONENT_ROCK:
                score += 2
            elif self.opponent_move == self.OPPONENT_PAPER:
                score += 3
            elif self.opponent_move == self.OPPONENT_SCISSORS:
                score += 1

        return score


def get_rock_paper_scissors_list() -> list[RockPaperScissorsGame]:
    rock_paper_scissors_list: list[RockPaperScissorsGame] = []

    with open(INPUT_FILE_NAME, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            moves_array = line.split(" ")
            rock_paper_scissors_list.append(RockPaperScissorsGame(moves_array[0], moves_array[1]))

    return rock_paper_scissors_list
