#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

#*Пример:*

#A = 3; B = 5 -> 243 (3⁵)
#    A = 2; B = 3 -> 8 


def exponen(A,B):
    if B <= 0:
            return 1
    return  A * exponen(A,(B-1))
A = int(input('Введите число А: '))
B = int(input('Введите степень: '))
        
print(f'A = {A},B = {B} -> {exponen(A,B)} ')