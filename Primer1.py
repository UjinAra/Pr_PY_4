# 1.Пользователь вводит число, нужно вывести чило pi с заданной
# точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)
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

nSpisok=dataInput("Введите точность вычисления числа ПИ - ")
pi=0
for i in range(nSpisok):
    pi += (1/16**i)*((4/(8*i+1))-(2/(8*i+4))-(1/(8*i+5))-(1/(8*i+6)))
print ("Пи -  ", round(pi,nSpisok))
    