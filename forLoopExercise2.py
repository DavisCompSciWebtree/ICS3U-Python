"""
Mr. Davis
In this exercise I would like you to have a list of 20 randomly
generating numbers (from 0-100). I then want you to print (1) the
length of your list, (2) the value of the largest number in you list,
and (3) the index position of the largest number.


"""

import random

randomList1 = [0]*20 #start with a known size and overwrite the values later
randomList2 = [] # start with an empty list and use ".append()"

for x in range(len(randomList1)):
    randomList1[x]= random.randint(0, 101)

print(randomList1)
print(len(randomList1))


for x in range(20):
    randomList2.append(random.randint(0, 101))

print(randomList2)
print(len(randomList2))

