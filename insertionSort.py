import random
import time
# this seed will keep my random numbers the same for all my attempts
random.seed(42)
unsortedRandomList = []
#Creating the random list
for i in range(10):
    unsortedRandomList.append(random.randint(-1000, 1001))

print(unsortedRandomList)


def insertion_sort(pList):
    for i in range(1, len(pList)):
        key = pList[i]
        j = i - 1
        print(f'{pList} Outside Top i={i} j={j} key={key}')

        while j >= 0 and key < pList[j]:
            print(f'{pList} Inside Top i={i} j={j} key={key}')

            pList[j + 1] = pList[j]
            j -= 1
            print(f'{pList} Inside Bot i={i} j={j} key={key}')
        pList[j + 1] = key
        print(f'{pList} Outside Bot i={i} j={j} key={key}')


insertion_sort(unsortedRandomList)

