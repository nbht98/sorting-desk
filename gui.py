#!/usr/bin/env python3
import pyglet
import time
import argparse
from pyglet.window import key


def printlst(lst):
    print(' '.join(map(str, lst)))


tempquick = []
valuequick = []


alllst = []
lstpos = []
count = 0
glotemp = 0
checkcolor = False
auto = flag = False

batch1 = pyglet.graphics.Batch()
window = pyglet.window.Window(fullscreen=True)


def getsprite(lst):
    lstsprite = {}
    for i in range(len(lst)):
        pos = i
        label = pyglet.text.Label(text="%s" % lst[i],
                                  x=pos * 130 / len(lst) * 15 +
                                  30 * 15 / len(lst),
                                  y=550, color=(255, 255, 3, 255),
                                  font_size=20 * 15 / len(lst))
        lstsprite[str(i)] = label
    return lstsprite


def bubble_sort(lst):
    templst = []
    value = []
    n = len(lst)
    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True
                templst.append([str(j), str(j + 1), True])
                value.append(False)
                printlst(lst)
            else:
                templst.append([str(j), str(j + 1), False])
        if swap is False:
            break
    return templst, value


def insertion_sort(lst):
    tempdict = []
    n = len(lst)
    for i in range(1, n):
        tempdict.append([])
        cur = lst[i]
        pos = i
        check = False
        while pos > 0 and lst[pos - 1] > cur:
            tempdict[i-1].append(str(pos))
            lst[pos] = lst[pos - 1]
            pos = pos - 1
            check = True
        lst[pos] = cur
        tempdict[i-1].append(str(pos))
        if check:
            printlst(lst)
    return tempdict


def insertintolst(lst):
    templst = []
    value = []
    for i in lst:
        if len(i) > 0:
            if len(i) == 1:
                templst.append([i[0], i[0], True])
                value.append(False)
            elif len(i) == 2:
                templst.append([i[1], i[0], True])
                value.append(False)
            else:
                for j in range(len(i)):
                    if j > 0:
                        templst.append([i[j], i[j-1], True])
                        value.append(False)
    return templst, value


def partition(lst, first, last):
    global tempquick
    global value
    pivot = (first + last) // 2
    tempquick.append([str(pivot), str(pivot), True])
    valuequick.append(False)
    lst[pivot], lst[first] = lst[first], lst[pivot]
    tempquick.append([str(pivot), str(first), 'Pivot'])
    valuequick.append(False)
    pivot = lst[first]
    lastS1 = first
    for firstunknown in range(first + 1, last + 1):
        if lst[firstunknown] < pivot:
            lastS1 += 1
            lst[firstunknown], lst[lastS1] = lst[lastS1], lst[firstunknown]
            tempquick.append([str(firstunknown), str(lastS1), True])
            valuequick.append(False)
        else:
            tempquick.append([str(firstunknown), str(firstunknown), False])
    lst[first], lst[lastS1] = lst[lastS1], lst[first]
    tempquick.append([str(first), str(lastS1), 'Pivot'])
    valuequick.append(False)
    print("P:", lst[lastS1])
    printlst(lst)
    return lastS1


def quick_sort(lst, first, last):
    if (first < last):
        pivotindex = partition(lst, first, last)
        quick_sort(lst, first, pivotindex - 1)
        quick_sort(lst, pivotindex + 1, last)


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


def getpos(lst, lstsprite):
    templst = []
    for i in lst:
        templst.append((lstsprite[i[0]].x, lstsprite[i[1]].x))
    return templst


def getvalue(lst):
    temp = []
    for i in lst:
        temp.append(False)
    return temp


def changecolor(a, b, color):
    a.color = color
    b.color = color


def move(a, b, x, y):
    global count
    global lstpos
    global lsts
    global flag
    if x > y:
        if a.x < x and b.x > y:
            changecolor(a, b, (255, 3, 3, 255))
            a.x += 5
            b.x -= 5
            return False
        else:
            changecolor(a, b, (255, 255, 3, 255))
            return True
    else:
        if a.x > x and b.x < y:
            changecolor(a, b, (255, 3, 3, 255))
            a.x -= 5
            b.x += 5
            return False
        else:
            changecolor(a, b, (255, 255, 3, 255))
            return True


def move_object(lstsprite):
    global count
    global glotemp
    global lstpos
    global value
    global alllst
    global checkcolor
    global flag, auto
    value[0] = True
    if count < len(value):
        if count >= 0 and (auto or flag):
            if checkcolor is True:
                checkcolor = False
                temp1 = lstsprite[alllst[glotemp - 1][0]]
                temp2 = lstsprite[alllst[glotemp - 1][1]]
                time.sleep(1)
                changecolor(temp1, temp1, (255, 255, 3, 255))
            a = lstsprite[alllst[glotemp][0]]
            b = lstsprite[alllst[glotemp][1]]
            if (alllst[glotemp][2] is True and value[count] is True) or \
               (alllst[glotemp][2] == 'Pivot' and value[count] is True):
                x = lstpos[glotemp][1]
                y = lstpos[glotemp][0]
                check = move(a, b, x, y)
                if check is False:
                    check = move(a, b, x, y)
                else:
                    flag = False
                    lstsprite[alllst[glotemp][0]], \
                        lstsprite[alllst[glotemp][1]] = \
                        lstsprite[alllst[glotemp][1]], \
                        lstsprite[alllst[glotemp][0]]
                    if alllst[glotemp][2] == 'Pivot':
                        changecolor(a, a, (255, 50, 150, 255))
                    elif a == b:
                        checkcolor = True
                        changecolor(a, b, (255, 3, 3, 255))
                    lstpos = getpos(alllst, lstsprite)
                    if count < len(value) - 1:
                        value[count + 1] = True
                    count += 1
                    glotemp += 1
            else:
                glotemp += 1
                checkcolor = True
                changecolor(a, b, (255, 3, 3, 255))
                flag = False
    if count == len(value) and (flag or auto):
        for i in lstsprite.keys():
            changecolor(lstsprite[i], lstsprite[i], (255, 255, 255, 255))


def update(_):
    global count
    global lstpos
    global lsts
    global flag
    global alllst
    global lstsprite
    global auto, flag
    if count == len(alllst):
        return
    move_object(lstsprite)


@window.event
def on_key_press(symbol, modifiers):
    global flag, auto
    if symbol == key.RIGHT:
        flag = True
    if symbol == key.SPACE:
        if auto:
            auto = False
        else:
            auto = True


@window.event
def on_draw():
    window.clear()
    for i in lstsprite.keys():
        lstsprite[i].draw()


def main():
    global count
    global lstpos
    global flag
    global alllst
    global lstsprite
    global value
    global flag, auto
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", help='specify\
     which algorithm to use for sorting among [bubble|insert|quick|merge],\
      default bubble', default='bubble')
    parser.add_argument("--gui", action='store_true', help='visualise\
     the algorithm in GUI mode')
    parser.add_argument('N', nargs='+', type=int)
    arg = parser.parse_args()
    lstsprite = getsprite(arg.N)
    if arg.algo == 'bubble':
        alllst, value = bubble_sort(arg.N)
        lstpos = getpos(alllst, lstsprite)
    elif arg.algo == 'insert':
        insertion_sort
        alllst, value = insertintolst(insertion_sort(arg.N))
        lstpos = getpos(alllst, lstsprite)
    elif arg.algo == 'merge':
        merge_sort(arg.N)
    elif arg.algo == 'quick':
        quick_sort(arg.N, 0, len(arg.N) - 1)
        alllst = tempquick
        value = valuequick
        lstpos = getpos(alllst, lstsprite)
    if arg.gui and arg.algo != 'merge':
        pyglet.clock.schedule_interval(update, 1/120)
        pyglet.app.run()


if __name__ == '__main__':
    main()
