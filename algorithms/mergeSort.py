import time
from colors import *

def merge(data, start, mid, end, drawData, timeTick, steps):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        steps = steps + 1
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        steps = steps + 1
        data[start] = tempArray[p]
        start += 1
    return steps

def merge_sort(data, start, end, drawData, timeTick, steps = 0):
    if start < end:
        mid = int((start + end) / 2)
        steps = merge_sort(data, start, mid, drawData, timeTick, steps)
        steps = merge_sort(data, mid+1, end, drawData, timeTick, steps)

        steps = merge(data, start, mid, end, drawData, timeTick, steps)

        drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid
        else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
    return steps