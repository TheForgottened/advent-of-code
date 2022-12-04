import operator


INPUT_FILE_NAME: str = "input.txt"

class Food:
    def __init__(self, calories: int):
        self.calories = calories

class Elf:
    def __init__(self):
        self.list_of_food: list[Food] = []

    def add_food(self, new_food: Food) -> None:
        self.list_of_food.append(new_food)

    @property
    def total_calories_carried(self) -> int:
        return sum([food.calories for food in self.list_of_food])

def get_sorted_elf_list() -> list[Elf]:
    elf_list: list[Elf] = []

    with open(INPUT_FILE_NAME, "r") as f:
        current_elf = Elf()
        for line in f:
            line = line.strip()

            if not line:
                elf_list.append(current_elf)
                current_elf = Elf()
                continue

            new_food = Food(int(line))
            current_elf.add_food(new_food)

        elf_list.append(current_elf)

    elf_list.sort(key=operator.attrgetter("total_calories_carried"))
    return elf_list
