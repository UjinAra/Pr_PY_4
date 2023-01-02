# 2. Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.
import sys

def dataInput(st):
    try:
      n = int(input(st)) # Число N
      if n==0:
        print("Вы ввели 0")
        sys.exit()  
    except ValueError:
        print("Вы ввели не число")
        sys.exit() 
    return n 

nSpisok=dataInput("Задайте натуральное число N - ")

i = 2  # первое простое число
spList = []
while i <= nSpisok:
    if nSpisok % i == 0:
        spList.append(i)
        nSpisok //= i
    else:
        i += 1
print(f"Список простых множителей: {spList}")