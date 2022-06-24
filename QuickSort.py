from random import random, seed, randint
from time import time

def isSorted(array, size):                                  # Проверка на упорядоченность
    for i in range (0, size - 1):
        if array[i] > array[i + 1]:
            return False
    return True

def printArray(array, size):                                # Вывод массива
    if isSorted(array, size):
        print('Sorted!')
    else:
        print('Unsorted!')
    for i in range (0, 10):
            print(array[i], end = '\n')
    print('\n')

def sort(array, start, end):                                # Сортировка массива
    if start <= end:
        mid = array[randint(start, end)]
        i = start
        j = end
        while i <= j:
            while array[i] < mid: i += 1
            while array[j] > mid: j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        sort(array, start, j)
        sort(array, i, end)

seed(time())                                                # Инициализация таймера
print('Input array size: ')
size = int(input())                                         # Размер массива
random_array = []
for i in range (0, size):                                   # Заполнение массива случайными числами
    random_array.append(random() * size)
printArray(random_array, size)

l = 0
r = size - 1

t1 = time()
sort(random_array, l, r)                                    # Сортировка
t2 = time()
elapsed = 1000 * (t2-t1)                                    # Время, затраченное на операцию, мс

printArray(random_array, size)
print('Time: ', elapsed, 'ms')
