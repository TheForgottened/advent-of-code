from common import get_rock_paper_scissors_list

games_list = get_rock_paper_scissors_list()
print(sum([game.my_score_initial_interpretation() for game in games_list]))
