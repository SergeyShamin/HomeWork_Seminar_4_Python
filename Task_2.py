'''Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
элементов исходной последовательности.
Посмотрели, что такое множество? Вот здесь его не используйте'''


import random


def look_up_number_in_list(list_of_numbers):
    result_list = []
    for number in list_of_numbers:
        if number not in result_list:
            result_list.append(number)
    return result_list


list_of_numbers = []
for i in range(1, 20): 
    list_of_numbers.append(random.randint(1, 10))

print(list_of_numbers)
print(look_up_number_in_list(list_of_numbers))