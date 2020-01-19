# print("hello") # python3
# print "hello"  # python2

# multiline comment does not exist (not supoorted) in python
"""
doc string area, used for documentaion, not multiline comment.
This function do ....
help() uses this to find things.
"""

# ; is only used because it allows for multiple statements on the same line.
# but this is discuraged

# white space and blocks in python NEED TO HAVE 4 SPACES

x = 2
if x == 2:
    print("x must be 2")
else:
    if x == 3:
        print("x must be 3")
    else:
        print("x is something else")

# theres no undefined in python
# else if => elif


def foo(x, y):
    print(x)
    return y

# print(foo(1,2))
# a = None
# b = ""
# a     this is not a thing


a = 12  # int
b = 1.2  # float
c = 'hello'  # string
d = "hello"  # string
e = False  # bool
f = None  # null value

# type casting
4 + int("4")  # 8

a = [1, 2, 3]
len(a)
print(a[-1])  # last item on list
print(a[:])  # : => slice operator *** can be done with strings
print(a[0:2])  # : => slice operator     inclusive : exclusive => [1, 2]
# a[1:2] => [2]


# lambda function
def add(x, y): return x + y


print(add(4, 5))


x = 12
print(f'x is {x}')  # f-strings, string interpolation (starts with f'string')
print(str(x) + str(5))

a1 = list()  # Empty list
a2 = list((88, 99))  # List of two elements
a3 = []  # Empty list
a4 = [10, 20, 30]  # List of 3 elements
a5 = [1, 2, "b"]  # No problem

print(a4[1])  # prints 20
a4[0] = 5  # change from 10 to 5
# a4[20] = 99; # ERROR: assignment out of range

# slice
print(a4[1:])
print(a4[2:2])
a[-1]  # last item in the array
a[-2:]  # last two items in the array
a[:-2]  # everything except the last two items

# touple
x = (1, 2, 3)
print(x[1])  # prints 2
y = (10,)  # A tuple of one element, comma required

# list comprehension
a = [1, 2, 3, 4, 5]
# Make a list b that is the same as list a:
b = [i for i in a]  # copies
# Make a list c that contains only the even elements of a:
c = [i for i in a if i % 2 == 0]
print(c)

# printf => %
print('abcd: %3d, efgh: %2.2f' % (1234, 12223.123))


# not can be used to test not truthy
print(not 0)  # true
print(not not 0)  # false
print(not 1)  # false
print(not None)  # true
print(not "0")  # false, perhaps unexpectedly
print(not "x")  # false


# range(start, stop, step)
# Use the range() function to count:
for i in range(10):
    print(i)  # Prints 0-9
for i in range(20, 30):
    print(i)  # Prints 20-29
for i in range(-10, 20, 3):
    print(i)  # Print every 3rd number from -10 to 19


# A list
aa = [10, 20, 30]
# Print 10 20 30
for i in aa:
    print(i)
# A dict
bb = {'x': 5, 'y': 15, 'z': 0}
# Print x y z (the keys of the dict)
for i in bb:
    print(i)
    print(bb[i])

# Print from 10 down through 0
xxx = 10
while xxx >= 0:
    print(xxx)
    xxx -= 1

# python 'switch' statement


def func1(): print("case 1 is hit")


def func2(): print("case 2 is hit")


def func3(): print("case 3 is hit")


funcs = {"alpha": 1, "bravo": 2, "charlie": 3}

print(funcs["bravo"])

# print([value for value in funcs.values()]["bravo"])


def happy_day(day): if day == "monday": return ":("


if day != "monday":
    return ":D"
print(happy_day("sunday")) print(happy_day("monday"))
