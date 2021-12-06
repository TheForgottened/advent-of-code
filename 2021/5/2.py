from typing import final

INPUT_FILE_NAME: final = "input.txt"
vents_dict: dict[tuple[int, int], int] = {}

def update_vents_map(coordinates: tuple[int, int]) -> None:
    if coordinates in vents_dict:
        vents_dict[coordinates] += 1
        return

    vents_dict[coordinates] = 1

with open(INPUT_FILE_NAME, 'r') as f:
    for line in f:
        numbers = [int(n) for n in line.replace(" -> ", ",").split(',')]
        
        curr_x: int = numbers[0]
        end_x: int = numbers[2]
        curr_y: int = numbers[1]
        end_y: int = numbers[3]

        while curr_x != end_x or curr_y != end_y:
            update_vents_map((curr_x, curr_y))

            if (curr_x < end_x):
                curr_x += 1
            elif (curr_x > end_x):
                curr_x -= 1
            
            if (curr_y < end_y):
                curr_y += 1
            elif (curr_y > end_y):
                curr_y -= 1

        update_vents_map((end_x, end_y))

print("Result: ", len([key for key in vents_dict.keys() if vents_dict[key] > 1]))
            