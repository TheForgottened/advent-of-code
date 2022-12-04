from common import get_sorted_elf_list

sorted_elf_list = get_sorted_elf_list()
top_three_calories = sorted_elf_list[-1].total_calories_carried +\
        sorted_elf_list[-2].total_calories_carried +\
        sorted_elf_list[-3].total_calories_carried

print(top_three_calories)
