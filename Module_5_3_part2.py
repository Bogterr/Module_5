# Первая часть кода в Module_5_3_part1.py
# https://github.com/Bogterr/Module_5/blob/2b895cac1dbe99664eb52b1837b8de3ee049716f/Module_5_3_part1.py

from Module_5_3_part1 import *

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

# Task_3
print("\nЗадание N°3: \n")

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
