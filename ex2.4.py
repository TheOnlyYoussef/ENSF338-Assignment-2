import matplotlib.pyplot as plt
import sys
import json
import time
import colorsys as c
import random
sys.setrecursionlimit(20000)
 
def func1(arr, low, high):
    if low < high:    
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
    return arr

def func2(array, start, end):
    p = array[random.randint(start, end)] 
    low = start + 1 
    high = end 
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1 
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else: 
            break
    array[start], array[high] = array[high], array[start]
    return high

def main():
    with open('ex2.json') as f:
        data = json.load(f)
        
    x = [len(data[i]) for i in range(len(data))]
    y = []
    
    for i in range(len(data)):
        start_time = time.time()
        if len(data[i]) <= 1000:
            data[i] = func1(data[i], 0, len(data[i])-1)
        else:
            partitions = len(data[i]) // 1000 + 1
            temp = []
            for j in range(partitions):
                start = j * 1000
                end = min(start + 1000, len(data[i]))
                partition = data[i][start:end]
                temp.extend(func1(partition, 0, len(partition)-1))
            data[i] = temp
        y.append(time.time() - start_time)
        
    plt.plot(x, y)
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity Plot')
    plt.show()

    #with open('ex2.5.json', 'w') as f:
        #json.dump(data, f)

if __name__ == "__main__":
    main()
