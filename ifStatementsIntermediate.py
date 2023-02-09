"""




"""

if True:
    print("the first thing is true")

if 1>0:
    print("one is always greater than zero, so this will always print")

if 5>0 and 5<0:
    print("this will never print, becasue they both need to be True, but both comparison")

if 5>0 or 5<0:
    print("this will always print because only 1 of the statements need to be true")

"""
Now for some slightly more advanced if statements


"""
hasCheeseBurger = True
hasDietCoke = True
hasDrPepper = True
hasVegan = False
hasVegetarian = True

if (hasVegan and hasDietCoke) or (hasCheeseBurger and hasDrPepper):
    print("Very Healthy or Very Unhealthy options")
elif(hasDrPepper):
    print("this will NOT print, because the first if will prevent")
else:
    print("this will happen if neither of the if or elif are true")

"""
Python also has some UNIQUE if statements that other languages don't have

"""

if '101' in "10010100":
    print(int("10010100",2))


