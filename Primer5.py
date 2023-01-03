# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random
import sys
import re

def mnogochlen (k,name):
    st= ""
    for i in range(k,0,-1):
        n = random.randint(-100,101)
        if n<0 or i==k:
            st= st + f"{n}x^{i}"
        elif n==0:
            st=st
        else:
            st= st + f"+{n}x^{i}"
    n = random.randint(-100,101)
    if n<0:
        st= st + f"{n}=0"
    elif n==0:
            st=st + "=0"
    else:
        st= st + f"+{n}=0"
    
    with open(name, 'w') as data:
        data.write(st)
        
def dataInput(st0):
    try:
      n = int(input(st0)) # Число N
      if n==0:
        print("Вы ввели 0")
        sys.exit()  
    except ValueError:
        print("Вы ввели не число")
        sys.exit() 
    return n 

def elections(a: tuple) -> dict:
    res = {}
    for i in a:
        res.setdefault(i[0],0)
        res[i[0]] += i[1]
    return res

def slovar(stSl):
    dSl={}
    stSl=stSl[2:len(stSl)-4]
    xCount=stSl.count("x")
    for i in range(xCount):
         n=stSl.find("x")
         a=int(stSl[n+2:n+2+len(str(xCount-i))])
         dSl[a]=int(stSl[:n])
         stSl=stSl[n+2+len(str(xCount-i)):]
    if stSl != "":
          dSl[0]=int(stSl)
    return dSl

mn1=dataInput("Задайте натуральное число K для 1 многочлена - ")
mn2=dataInput("Задайте натуральное число K для 2 многочлена - ")
mnogochlen(mn1,"fl34_1.txt")
mnogochlen(mn2,"fl34_2.txt")

with open('fl34_1.txt', 'r') as data:
    st1 = str(data.readlines())
with open('fl34_2.txt', 'r') as data:
    st2 = str(data.readlines())

print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")

d1={}
if len(st1)>len(st2):
    d1=elections(list(slovar(st1).items())+list(slovar(st2).items()))
else:
    d1=elections(list(slovar(st2).items())+list(slovar(st1).items()))

stRes=""
s=""
for key in d1:
    if d1[key]>0:
        s="+"+str(d1[key])
    else: 
        s=str(d1[key])
    if key ==0:
        s=s+"=0"  
    else:
        s=s+"x^"+str(key)     
    stRes=stRes + s

print(stRes)

with open('fl34_rez.txt', 'w') as data:
     data.write(stRes)   



