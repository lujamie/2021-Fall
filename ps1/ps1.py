#arr is array of (val, key) pairs
import math
import time
import random


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

# v2
def countSort2(arr, univsize):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

# v1
def countSort1(arr, univsize, ind=-1):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        if ind != -1:
            universe[elt[0][ind]].append(elt)
        else:
            universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)
    return sortedArr

def baseConvert(num, b, U):
    remainder = []

    while num > 0:
        remainder.append(num % b)
        num = num // b

    new_num = []
    for r in range(len(remainder)):
        new_num.append(remainder[r])

    size = len(new_num)
    tot_size = int(math.log(U, b))
    for i in range(tot_size - size + 1):
        new_num.append(0)

    return new_num

def radixSort(arr, n, U):
    if len(arr) == 1 or len(arr) == 0:
        return arr

    for i in range(0, math.ceil(math.log(U, n))):
        convertedArr = []
        for (key, item) in arr:
            convertedArr.append((baseConvert(key, n, U), [key, item]))
        arr = convertedArr
        radixArr = []
        for (digits, pair) in arr:
            radixArr.append((digits[i], pair))
        sortedRadix = countSort2(radixArr, n)
        arr = []
        for (digit, pair) in sortedRadix:
            key, item = pair
            arr.append((key, item))
    return arr




# arr = [(5, 0), (16, 1), (100, 2), (34, 3)]
# arr = [(170, 'a'), (45, 'b'), (75, 'c'), (90, 'd'), (802, 'e'), (24, 'f'), (2, 'g'), (66, 'h')]

# print("Succes?", radixSort(arr, 4, 1000))
# print(countSort1(arr, 110))
