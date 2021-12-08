from typing import final

INPUT_FILE_NAME: final = "input.txt"
nr_segments_one: final = 2
nr_segments_four: final = 4
nr_segments_seven: final = 3
nr_segments_eight: final = 7
digit_input_value: list[list[str]] = []
four_digit_output_value: list[list[str]] = []

with open(INPUT_FILE_NAME) as f:
    for line in f:
        input_output = line.strip().split(' | ')
        digit_input_value.append(input_output[0].split(' '))
        four_digit_output_value.append(input_output[1].split(' '))

output_sum: int = 0
for i in range(len(digit_input_value)):
    digit_zero: str
    digit_one: str = "".join(sorted([string for string in digit_input_value[i] if len(string) == nr_segments_one][0]))
    digit_two: str
    digit_three: str
    digit_four: str = "".join(sorted([string for string in digit_input_value[i] if len(string) == nr_segments_four][0]))
    digit_five: str
    digit_six: str
    digit_seven: str = "".join(sorted([string for string in digit_input_value[i] if len(string) == nr_segments_seven][0]))
    digit_eight: str = "".join(sorted([string for string in digit_input_value[i] if len(string) == nr_segments_eight][0]))
    digit_nine: str

    segment_group_c_f: list[str] = [char for char in digit_one] 

    segment_a: str = [char for char in [string for string in digit_input_value[i] if len(string) == nr_segments_seven][0] if char not in digit_one][0]

    digit_three = "".join(sorted([string for string in digit_input_value[i] if len(string) == 5 and all(char in string for char in digit_one)][0]))
    segment_group_d_g: list[str] = [char for char in digit_three if char != segment_a and char not in segment_group_c_f]

    digit_nine = "".join(sorted([string for string in digit_input_value[i] if len(string) == 6 and all(char in string for char in segment_group_c_f) and all(char in string for char in segment_group_d_g) and segment_a in string][0]))
    segment_b: str = [char for char in digit_nine if char not in segment_group_c_f and char not in segment_group_d_g and char != segment_a][0]

    segment_d: str = [char for char in digit_four if char not in segment_group_c_f and char != segment_b][0]

    segment_g: str = [char for char in segment_group_d_g if char != segment_d][0]

    digit_five = "".join(sorted([string for string in digit_input_value[i] if len(string) == 5 and all(char in string for char in [segment_a, segment_b, segment_d, segment_g] or char in segment_group_c_f)][0]))
    segment_f: str = [char for char in [char for char in digit_five if char in segment_group_c_f] if char in digit_five][0]
    segment_c: str = [char for char in segment_group_c_f if char != segment_f][0]

    segment_e: str = [char for char in digit_eight if char != segment_a and char != segment_b and char != segment_c and char != segment_d and char != segment_f and char != segment_g][0]

    digit_zero = "".join(sorted([string for string in digit_input_value[i] if len(string) == 6 and segment_d not in string][0]))
    digit_two = "".join(sorted([string for string in digit_input_value[i] if len(string) == 5 and segment_a in string and segment_c in string and segment_d in string and segment_e in string and segment_g in string][0]))
    digit_six = "".join(sorted([string for string in digit_input_value[i] if len(string) == 6 and segment_a in string and segment_b in string and segment_d in string and segment_e in string and segment_f in string and segment_g in string][0]))

    digits_array: list[str] = [digit_zero, digit_one, digit_two, digit_three, digit_four, digit_five, digit_six, digit_seven, digit_eight, digit_nine]

    number: int = 0
    multiplier: int = 1000
    for digit in four_digit_output_value[i]:
        sorted_digit: str = "".join(sorted(digit))
        number += digits_array.index(sorted_digit) * multiplier
        multiplier /= 10

    output_sum += number

print("Result: " + str(output_sum))