import random
import time

random.seed(42)
unsortedRandomList = []
#Creating the random list
for i in range(10):
    unsortedRandomList.append(random.randint(-1000, 1001))

print(unsortedRandomList)


def bubbleSort(pList):
    print(f'{pList} Start of function')
    n = len(pList)
    for i in range(n):
        print(f'{pList} Outside Top i={i}')
        for j in range(0, n-i-1):
            if pList[j] > pList[j+1]:
                #pList[j], pList[j+1] = pList[j+1], pList[j]
                temp = pList[j]
                pList[j] = pList[j+1]
                pList[j+1] = temp

            print(f'{pList} Inside Bottom i={i} j={j}')


        print(f'{pList} Outside Bottom i={i}')


bubbleSort(unsortedRandomList)