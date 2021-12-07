from typing import final
from statistics import mean
from math import floor

INPUT_FILE_NAME: final = "input.txt"
crab_horizontal_positions: list[int] = []

def get_crab_fuel_cost(steps: int) -> int:
    fuel_cost: int = 0

    for i in range(steps):
        fuel_cost += i + 1

    return fuel_cost

with open(INPUT_FILE_NAME) as f:
    crab_horizontal_positions = [int(n) for n in f.readline().split(',')]

crab_horizontal_positions.sort()
crab_horizontal_average_position: int = int(floor(mean(crab_horizontal_positions)))

fuel_cost_lower: int = 0

for n in crab_horizontal_positions:
    fuel_cost_lower += get_crab_fuel_cost(abs(n - crab_horizontal_average_position))

fuel_cost_higher: int = 0

for n in crab_horizontal_positions:
    fuel_cost_higher += get_crab_fuel_cost(abs(n - crab_horizontal_average_position))

print("Result: " + str(fuel_cost_lower if fuel_cost_lower > fuel_cost_higher else fuel_cost_higher))