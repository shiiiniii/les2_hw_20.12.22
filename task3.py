# Реализуйте алгоритм перемешивания списка. 

from random import sample
my_list = [0, 1, 2, 3, 4]
print(f"Изначальный список: {my_list}")
for i in range(1):
    num = range(5)
    new_list = sample(num, len(num))
    print(f"Перемешанный список: {new_list}")

