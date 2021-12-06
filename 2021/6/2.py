from typing import final

INPUT_FILE_NAME: final = "input.txt"
SIMULATION_DAYS: final = 256
MAX_FISH_TIMER: final = 8
FISH_TIMER_RESET_DEFAULT: final = 6
lanternfish_dict: dict[int, int] = {}

def initialize_lanternfish_dict() -> None:
    for i in range(0, MAX_FISH_TIMER + 1):
        lanternfish_dict[i] = 0

def add_lanternfish(lanternfish: int) -> None:
    if lanternfish in lanternfish_dict:
        lanternfish_dict[lanternfish] += 1
    else:
        lanternfish_dict[lanternfish] = 1

def next_simulation_day() -> None:
    number_fish_before: int = lanternfish_dict[MAX_FISH_TIMER]
    for i in range(MAX_FISH_TIMER, 0, -1):
        temp: int = lanternfish_dict[i - 1]
        lanternfish_dict[i - 1] = number_fish_before
        number_fish_before = temp

    # number_fish_before is now equal to the number of fish that had 0 days till a new cycle
    # Meaning they will reproduce and reset this timer
    lanternfish_dict[MAX_FISH_TIMER] = number_fish_before
    lanternfish_dict[FISH_TIMER_RESET_DEFAULT] += number_fish_before

initialize_lanternfish_dict()
with open(INPUT_FILE_NAME, 'r') as f:
    for line in f:
        numbers = [int(n) for n in line.split(',')]

        for n in numbers:
            add_lanternfish(n)

for i in range(SIMULATION_DAYS):
    next_simulation_day()

sum = 0
for key in lanternfish_dict:
    sum += lanternfish_dict[key]

print("Result: ", sum)
            