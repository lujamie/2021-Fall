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
        elif arr1[i][0] >= arr2[j][0]:
            sortedArr.append(arr2[j])
            j += 1
        else:
            sortedArr.append(arr1[i])
            i += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(arr, univsize, ind=-1):
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