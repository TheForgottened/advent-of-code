from typing import final

INPUT_FILE_NAME: final = "input.txt"
nr_segments_one: final = 2
nr_segments_four: final = 4
nr_segments_seven: final = 3
nr_segments_eight: final = 7
four_digit_output_value: list[list[str]] = []

with open(INPUT_FILE_NAME) as f:
    for line in f:
        four_digit_output_value.append(line.strip().split(' | ')[1].split(' '))

unique_segments: list[int] = [nr_segments_one, nr_segments_four, nr_segments_seven, nr_segments_eight]
flatten_four_digit_output_value = sum(four_digit_output_value, [])
print("Result: " + str(len([digit for digit in flatten_four_digit_output_value if len(digit) in unique_segments])))