import random
import time

random.seed(42)
unsortedRandomList = []
#Creating the random list
for i in range(10):
    unsortedRandomList.append(random.randint(-1000, 1001))

print(unsortedRandomList)

def selection_sort(pList):
    print(f'{pList} Start of function')
    n = len(pList)
    tempValue = 0
    for i in range(n):
        print(f'{pList} Outside i={i} ')
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            print(f'{pList} Inside i={i} j={j}')
            if pList[j] < pList[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        tempValue = pList[min_idx]
        pList[min_idx] = pList[i]
        pList[i] = tempValue

    return pList

selection_sort(unsortedRandomList)