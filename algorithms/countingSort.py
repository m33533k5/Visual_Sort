import time
from colors import *

def counting_sort(data, drawData, timeTick):
    steps = 0
    n = max(data) + 1
    count = [0] * n
    for item in data:
        count[item] += 1
        steps = steps + 1

    k = 0
    for i in range(n):
        for j in range(count[i]):
            data[k] = i
            drawData(data, [BLUE for x in range(len(data))] )
            time.sleep(timeTick)
            k += 1
            steps = steps + 1

    drawData(data, [BLUE for x in range(len(data))])
    return steps