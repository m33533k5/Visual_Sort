import time
from colors import *

def partition(data, start, end, drawData, timeTick, steps):
    i = start + 1
    pivot = data[start]
    steps = steps + 1 #Initialisierung des Pivots

    for j in range(start+1, end+1):
        steps = steps + 1 #Vergleich
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i+=1
            steps = steps + 1 #Vertauschung
    data[start], data[i-1] = data[i-1], data[start]
    steps = steps + 1 #Letzte Vertauschung Pivot
    return i-1, steps

def quick_sort(data, start, end, drawData, timeTick, steps = 0):
    if start < end:
        pivot_position, steps = partition(data, start, end, drawData, timeTick, steps)
        steps = quick_sort(data, start, pivot_position-1, drawData, timeTick, steps)
        steps = quick_sort(data, pivot_position+1, end, drawData, timeTick, steps)

        drawData(data, [PURPLE if x >= start and x < pivot_position else YELLOW if x == pivot_position
        else DARK_BLUE if x > pivot_position and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
    return steps