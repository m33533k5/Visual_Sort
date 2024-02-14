import time
from colors import *

def heapify(data, n, i, drawData, timeTick, steps):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and data[i] < data[left]:
        largest = left
        steps = steps + 1

    if right < n and data[largest] < data[right]:
        largest = right
        steps = steps + 1

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        steps = steps + 1
        steps = heapify(data, n, largest, drawData, timeTick, steps)
    return steps


def heap_sort(data, drawData, timeTick):
    n = len(data)
    steps = 0

    for i in range(n-1, -1, -1):
        steps = heapify(data, n, i, drawData, timeTick, steps)

    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        steps = steps + 1
        heapify(data, i, 0, drawData, timeTick, steps)
        drawData(data, [YELLOW if x == i else BLUE for x in range(n)])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
    return steps
