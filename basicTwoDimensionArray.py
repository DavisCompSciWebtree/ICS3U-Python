"""
Create a "2D Array" that is 7 wide and 5 tall
2. Along the Border of the Array, write a wall function that
makes the border an "X" or a unicode icon of your choice.
3. Randomly Generate a starting position with the center 2x2 or 3x3 region

"""
player = "P"
print(player)
print(chr(128992), chr(128993), chr(128994), chr(128995), chr(128996), chr(128997),
      chr(128998), chr(128999), chr(129000), chr(129001), chr(129002), chr(129003))
print(chr(9994), chr(9995), chr(9996))
print(chr(128584), chr(128585), chr(128586))
print(chr(128695), chr(128721))

#creating a 2D Array in Python
#Technically the the most intuitive way to make a 2D array, causes a lot of problems later on
#when a simple and logical solution does not work, this is called an Anti-Pattern
rows, columns = (7, 5)
nestedListA = [[chr(128999)]*columns]*rows

nestedListB = [[chr(129001) for x in range(columns)] for y in range(rows)]
print(nestedListA)

newGridA = nestedListA
newGridB = nestedListB


for row in nestedListA:
    print(row)

for row in nestedListB:
    print(row)

print()
for x in range(rows):
    for y in range(columns):
        if x == 0 or x == rows-1:
            newGridA[x][y] = chr(128721)



for row in newGridA:
    print(row)

print()
for x in range(rows):
    for y in range(columns):
        if x == 0 or x == rows-1:
            newGridB[x][y] = chr(128721)

for row in newGridB:
    print(row)


