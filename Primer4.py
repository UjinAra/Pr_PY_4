# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.


import random

k = int(input("Введите натуральную степень k = "))
st= ""
for i in range(k,0,-1):
    if i==k:
        st= st + f"{random.randint(0,101) }x^{i} "
    else:
        st= st + f"+ {random.randint(0,101) }x^{i} "
st= st + f"+ {random.randint(0,101)} = 0"

with open('fl33.txt', 'w') as data:
     data.write(st)


