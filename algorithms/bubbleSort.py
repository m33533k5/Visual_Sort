import time

from colors import YELLOW, BLUE


def bubble_sort(data, drawData, timeTick):
    size = len(data)
    steps = 0
    for i in range(size-1):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))] )
                steps = steps + 1
                time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
    return steps