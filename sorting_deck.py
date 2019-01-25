#!/usr/bin/env python3
import argparse


def printlst(lst):
    print(' '.join(map(str, lst)))


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True
                printlst(lst)
        if swap is False:
            break


def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        cur = lst[i]
        pos = i
        check = False
        while pos > 0 and lst[pos - 1] > cur:
            lst[pos] = lst[pos - 1]
            pos = pos - 1
            check = True
        lst[pos] = cur
        if check:
            printlst(lst)


def merge(lst, L, R):
    i = j = index = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            lst[index] = L[i]
            i += 1
        else:
            lst[index] = R[j]
            j += 1
        index += 1
    while i < len(L):
        lst[index] = L[i]
        i += 1
        index += 1
    while j < len(R):
        lst[index] = R[j]
        j += 1
        index += 1
    printlst(lst)


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        L = lst[:mid]
        R = lst[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(lst, L, R)


def partition(lst, first, last):
    pivot = (first + last) // 2
    lst[pivot], lst[first] = lst[first], lst[pivot]
    pivot = lst[first]
    lastS1 = first
    for firstunknown in range(first + 1, last + 1):
        if lst[firstunknown] < pivot:
            lastS1 += 1
            lst[firstunknown], lst[lastS1] = lst[lastS1], lst[firstunknown]
    lst[first], lst[lastS1] = lst[lastS1], lst[first]
    print("P:", lst[lastS1])
    printlst(lst)
    return lastS1


def quick_sort(lst, first, last):
    if (first < last):
        pivotindex = partition(lst, first, last)
        quick_sort(lst, first, pivotindex - 1)
        quick_sort(lst, pivotindex + 1, last)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", help='specify\
     which algorithm to use for sorting among [bubble|insert|quick|merge],\
      default bubble', default='bubble')
    parser.add_argument("--gui", action='store_true', help='visualise\
     the algorithm in GUI mode')
    parser.add_argument('N', nargs='+', type=int)
    arg = parser.parse_args()
    if arg.algo == 'bubble':
        bubble_sort(arg.N)
    elif arg.algo == 'insert':
        insertion_sort(arg.N)
    elif arg.algo == 'merge':
        merge_sort(arg.N)
    elif arg.algo == 'quick':
        quick_sort(arg.N, 0, len(arg.N) - 1)


if __name__ == '__main__':
    main()
