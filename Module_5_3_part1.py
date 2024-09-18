# Developer - не только разработчик
# Продолжение кода Module_5_3_part2
# https://github.com/Bogterr/Module_5/blob/4623bb1ae3b0f75f6bbc01ebfab78330519ad92a/Module_5_3_part2.py

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors and new_floor > 1:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __iadd__(self, value):
        return self + value

    def __radd__(self, value):
        return self + value
