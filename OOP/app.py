import functools
x = [1, 2, 3, 4, 5, 6]

y = functools.reduce(lambda x, y: x+y, x)
# print(y)

# all datatypes are objects

# self points to the object ***
class Person:                                                  # class
    def __init__(self, name, gender, job):                     # constructor (initializer function)
        print("I was born")

        self.name = name
        self.gender = gender
        self.job = job

    def info(self):                     # method (function in a class)
        print(f"{self.name}, {self.gender}, {self.job}")

    def gotJob(self, job):
        self.job = job


# a = Person()                            # object, instance of Person
# print(type(a))


# 
stev = Person("Steven", "Male", "Student")
jef = Person("Jeff", "Male", "Programmer")
print(id(stev))
print(id(jef))

jef.info()                              # shortcut (a is an obj with info already in) && most often used
# Person.info(jef)                      # gets translated to this
stev.info()