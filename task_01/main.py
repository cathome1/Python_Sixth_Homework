# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
from random import sample


s = int(input("Введите размер списка: "))
def MakeArray(size):
    arr = sample(range(0,size*2), size)
    return arr
array = MakeArray(s)
print(array)
def MaxArray(arr):
    j = arr[0]
    res = []
    for i in range(1,len(arr)):
        if arr[i]>j:
            res.append(arr[i])
        j = arr[i]
    return res
print(MaxArray(array))
