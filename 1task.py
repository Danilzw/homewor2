#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.
import random

size1 = int(input("Введите размер1:"))

size2 = int(input("Введите размер2:"))

array1 = []

array2 = []

resultarray = []

for i in range(size1):
    array1.append(random.randint(1,9))
for i in range(size2):
    array2.append(random.randint(1,9))

print(array1,array2)

for i in range(len(array1)):
    for j in range(len(array2)):
        if array1[i] in resultarray:
            continue
        if array1[i] == array2[j]:
            resultarray.append(array1[i])

resultarray.sort()
print(resultarray)

