from typing import final
from statistics import median

INPUT_FILE_NAME: final = "input.txt"
crab_horizontal_positions: list[int] = []

with open(INPUT_FILE_NAME) as f:
    crab_horizontal_positions = [int(n) for n in f.readline().split(',')]

crab_horizontal_positions.sort()
crab_horizontal_median_position: int = median(crab_horizontal_positions)

fuel_cost: int = 0

for n in crab_horizontal_positions:
    fuel_cost += abs(n - crab_horizontal_median_position)

print("Result: " + str(fuel_cost))