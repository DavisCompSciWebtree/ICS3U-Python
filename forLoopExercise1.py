"""
For some reason, the internet culture thinks it's cool to replace
perfectly acceptable letters with numbers. You know, replace "E" with "3";
replace "i" or "l" with "1" or "!". I don't know, I guess they think it's
a sign of creativity or maybe it scratches an itch from their
overdeveloped teenage angst.

Any here's the exercise. Write a program that allows
the user to input the name of their favorite Disney movie, then
they print out the original movie title, and the modified
version of the name.

replace
a with @
E with 3
i or l with 1 or !
s with 5
b with 6
L with 7
o with 0

You will need input(), for loop, here is some example code
to get you thinking. Comment it out when you are done learning.


"""

# Using replace() method
string = "Bubblegum"

# replacing the 'b' character with 'B'
changedString = string.replace("b", "B", 1)

print("Original string: ", string)
print("New string: ", changedString)