'''Задайте натуральное число N. Напишите программу, 
которая составит список простых множителей числа N.
Пример: при N = 12 -> [2, 3]'''

from functions import input_number_test

def prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

number = input_number_test("Введите число : ")

def denominator(num):
    list_denominators = []
    for i in range(2, num):
        if num % i == 0 and prime_number(i): 
            list_denominators.append(i)
    return list_denominators

print(prime_number(number))
print(denominator(number))