# Python: 2.7.12
#
# Author: Tom Stock
#
# Purpose: I'm making this program to test out my  basic skills with Python, enjoy :)
#          




# Assign an integer to a variable:
a = 10

# Assign a string to a variable:
b = "This is a string."

# Assign a float to a variable:
c = 17.5

# Use the print function and .format() notation to print out the assigned variable
print ("variable a is the integer {}, variable b is the string '{}',".format(a,b))
print  ("variable c is the floating point number {}.".format(c))

# Time to do some math! (use operators +,-,*,/,+=,=,%)
d = 8 + 4 - 10  # This equals 2
e = 3 * 8 / 6   # This equals 4
f = d + e % 4   # 2 is left over (modulus)
print f

d += e     #d is now 6
print d

g = e + f # This should equal 6, just showing I know how to use an equal sign.
print g

# Use logical operators: and, or, not

if (5 > 2) and (6 < 7): # both expressions are true so the next part prints
    print "Great use of AND"


if (3 > 5) or ((3 - 1) == 2): # at least one expression is true so the next part prints
    print "This OR is true"

h = not (1 == 1) # normally expression would return true, the 'not' makes it opposite (false).
print h


# Using if, elf, else:
x = 20
if (x < 20):
    print "x is less than 20"
elif (x > 20):
    print "x is greater than 20"
else:
    print "x equals 20"

# Use while loop:
cars=0
while(cars<5):
    print "The number of cars is: ", cars
    cars = cars + 1
print "That's all of the cars!"

# Use for loop:
boats=0
for boats in range(0,4):
    print "There are ", boats,"boats."

# Create a list, iterate through list using a for loop to print out each item in list on a new line
ice_cream_flavors = ["chocolate", "vanilla", "strawberry", "pineapple"]
for flavor in ice_cream_flavors:
    print "I like", flavor, "flavored ice cream!"

# Create a tuple, iterate through it using a for loop to print out each item on a new line:
tv_shows = ('Breaking Bad', 'Game of Thrones', 'Silicon Valley')
for show in tv_shows:
    print show, "is a great TV show!"

# Define a function that returns a string variable:

def adding(j,k):
    add = j + k
    return str(add)

print adding(10, 3)



