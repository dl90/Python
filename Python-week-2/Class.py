# a list of strings
animals = ['cat', 'dog', 'fish', 'bison']

# a list of integers
numbers = [1, 7, 34, 20, 12]

# an empty list
my_list = []

# Array = fixed size, List = auto-resize
# memory allocation is the reason behind why some lists enforce type


print(animals[0]) # cat
print(numbers[1]) # 7

# This will give us an error, because the list only has four elements
print(animals[6])

print(animals[-1]) # the last element -- bison
print(numbers[-2]) # the second-last element -- 20

print(animals[1:3]) # ['dog', 'fish']
print(animals[1:-1]) # ['dog', 'fish']

print(animals[2:]) # ['fish', 'bison']
print(animals[:2]) # ['cat', 'dog']
print(animals[:]) # a copy of the whole list

print(animals[::2]) # ['cat', 'fish'] Specify the step size with a third param

# Lists are mutable – we can modify elements, add elements to them or remove elements from them.
#  A list will change size dynamically when we add or remove elements
# – we don’t have to manage this ourselves


# assign a new value to an existing element
animals[3] = "hamster"

# add a new element to the end of the list
animals.append("squirrel")

# remove an element by its index
del animals[2] # shrink/resize the list

####### why copy a list?
animals = ['cat', 'dog', 'goldfish', 'canary']
pets = animals # now both variables refer to the same list object

animals.append('aardvark')
print(pets) # pets is still the same list as animals

animals = ['rat', 'gerbil', 'hamster'] # now we assign a new list value to animals
print(pets) # pets still refers to the old list

pets = animals[:] # assign a *copy* of animals to pets
animals.append('aardvark')
print(pets) # pets remains unchanged, because it refers to a copy, not the original list


#### Check whether a list contains a particular value
numbers = [34, 67, 12, 29]
my_number = 67

if number in numbers:
    print("%d is in the list!" % number)

my_number = 90
if number not in numbers:
    print("%d is not in the list!" % number)

#### Built in List methods
# the length of a list
len(animals)

# the sum of a list of numbers
sum(numbers)

# are any of these values true?
any([1,0,1,0,1])

# are all of these values true?
all([1,0,1,0,1])


##########
numbers = [1, 2, 3, 4, 5]

# we already saw how to add an element to the end
numbers.append(5)

# count how many times a value appears in the list
numbers.count(5)

# append several values at once to the end
numbers.extend([56, 2, 12])

# find the index of a value
numbers.index(3)
# if the value appears more than once, we will get the index of the first one
numbers.index(2)
# if the value is not in the list, we will get a ValueError!
numbers.index(42)

# insert a value at a particular index
numbers.insert(0, 45) # insert 45 at the beginning of the list

# remove an element by its index and assign it to a variable
my_number = numbers.pop(0)

# remove an element by its value
numbers.remove(12)
# if the value appears more than once, only the first one will be removed
numbers.remove(5)

### Sorting or reversing a List
numbers = [3, 2, 4, 1]

# these return a modified copy, which we can print
print(sorted(numbers))
print(list(reversed(numbers)))

# the original list is unmodified
print(numbers)

# now we can modify it in place
numbers.sort()
numbers.reverse()

print(numbers)

### Tuples ** significantly more performant than lists

WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
animals = ('cat', 'dog', 'fish')
# convert touples to list
abc = list(WEEKDAYS)

# an empty tuple
my_tuple = ()

# we can access a single element
print(animals[0])

# we can get a slice
print(animals[1:]) # note that our slice will be a new tuple, not a list

# we can count values or look up an index
animals.count('cat')
animals.index('cat')

# ... but this is not allowed:
animals.append('canary')
animal[1] = 'gerbil'

# What are tuples good for? We can use them to create a sequence of values that we don’t
# want to modify. For example, the list of weekday names is never going to change. If we
# store it in a tuple, we can make sure it is never modified accidentally in an unexpected place

# Here's what can happen if we put our weekdays in a mutable list

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def print_funny_weekday_list(weekdays):
    weekdays[5] = 'Caturday' # this is going to modify the original list!
    print(weekdays)

print_funny_weekday_list(WEEKDAYS)

print(WEEKDAYS) # oops

# How do we define a tuple with a single element? 
print(3)
print((3)) # this is still just 3

# solution (single element touple) **
print((3,))

###### Sets

# A set is a collection of unique elements. If we add multiple copies of the same element to a set,
# the duplicates will be eliminated, and we will be left with one of each element
# sets use { }

animals = {'cat', 'dog', 'goldfish', 'canary', 'cat'}
print(animals) # the set will only contain one cat

even_numbers = {2, 4, 6, 8, 10}
big_numbers = {6, 7, 8, 9, 10}

# subtraction: big numbers which are not even
print(big_numbers - even_numbers)

# union: numbers which are big or even
print(big_numbers | even_numbers)

# intersection: numbers which are big and even
print(big_numbers & even_numbers)

# numbers which are big or even but not both
print(big_numbers ^ even_numbers)

# It is important to note that unlike lists and tuples sets are not ordered.
# When we print a set, the order of the elements will be random. If we want to process the contents
# of a set in a particular order, we will first need to convert it to a list or tuple and sort it

print(animals)
print(sorted(animals))

##### Dictionaries
marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

personal_details = {
    "name": "Jane Doe",
    "age": 38, # trailing comma is legal
}

print(marbles["green"])
print(personal_details["name"])

# This will give us an error, because there is no such key in the dictionary
print(marbles["blue"])

# modify a value
marbles["red"] += 3
personal_details["name"] = "Jane Q. Doe"

surnames = {} # this is an empty dictionary
surnames["John"] = "Smith"
surnames["John"] = "Doe"
print(surnames) # we overwrote the older surname

marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }
marbles["blue"] = 30 # this will work
marbles["purple"] += 2 # this will fail -- the increment operator needs an existing value to modify!

# Like sets, dictionaries are not ordered – if we print a dictionary, the order will be random.

# Common Dictionary Methods
marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

# Get a value by its key, or None if it doesn't exist
marbles.get("orange")
# We can specify a different default
marbles.get("orange", 0)

# Add several items to the dictionary at once
marbles.update({"orange": 34, "blue": 23, "purple": 36})

# All the keys in the dictionary
marbles.keys()
# All the values in the dictionary
marbles.values()
# All the items in the dictionary
marbles.items()

# We can check if a key is in the dictionary
print("purple" in marbles)
print("white" not in marbles)

# We can also check if a value is in the dictionary 
print("Smith" in surnames.values())


# Strings Continued

# We can easily convert a string to a list of characters
abc_list = list("abracadabra")


# Observe what the join method does
l = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

s = "".join(l)
print(s)

animals = ('cat', 'dog', 'fish')

# a space-separated list
print(" ".join(animals))

# a comma-separated list
print(",".join(animals))

# a comma-separated list with spaces
print(", ".join(animals))

# The opposite of join is split
print("cat|dog|fish".split("|"))