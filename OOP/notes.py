a = 0 # global


def my_function():
    local = 10  # enclosed scope

    def func():
        nonlocal local
        local = 20

        def func1():
            nonlocal local
            local = 30

            def func2():
                global a
                a = 100

            func2()
        func1()
    func()
    return local

# print(a)
# print(a + my_function())
# print(a)


class pas:                  # passing a class
    pass

# without a constructor, python creates a default constructor
# use of constructors is to enforce setting instance variables (all instances must have to create)
# instance variables allow for unique objects
class Dog:
    species = "dog"         # class variable = all instances share this
    def bark(self):         # instance method
        print("bark")

doggo = Dog()
doggo.name = "Doggo"        # python allows adding attributes after obj creation


class employee:
    def __init__(self, name, sal, x):
        self.name=name
        self._salary=sal    # _ implies this is a protected attribute
        self.__secret = x   # __ implies private attribute
    
    def greet():                # private attributes can be accessed within class 
        print(self.__secret)

    # def getSecret(self):        # getter function
    #     return self.__secret

    # def setSecret(self, xx):    # setter function
    #     self.__secret = xx

    # secret = property(getSecret, setSecret)     # exposes secret as a property (ordering can be set fget = getMethod, fset= setMethod)

    #decorators => don't have to explicitly call property
    @property                   # getter
    def secret(self):
        return self.__secret

    @secret.setter                # setter
    def secret(self, val):
        self.__secret = val

e = employee("test", 1, 2)
e.secret = "secret"
print(e.secret)


emp1 = employee("Sam", 1000, 12)
# emp1.salary = 2000
# print(emp1.__secret)      # errors

# emp1.__secret = 321
# print(emp1.__secret)

# Name Mangeling
# emp2 = employee("test", 2000, 13)
# print(emp2._employee__secret)   # prints
# __secret => obj._class__attribute

# emp2.__secret = 3232    # python litterally sets a new attribute __secret
# print(emp2.__secret)    # accessing the new variable

# print(emp2.__dict__)    # prints a dictionary representation of the instance


# emp2.setSecret(123)
# emp2.secret = 32
# print(emp2.secret)      # enabled with properties




# the last function gets executed if the same namespace is used in multiple javascript files linked to an html file
# script1.js script2.js script3.js 
# namespace info leak into eachother file


# Scoping

# Local
# Enclosed
# Global
# Built-in
# accessing built in primitives form Python print()

# LEGB Rule
# look up scope order (local, enclosed, global, built-in)

# Nested Functions -> Closures
def outi():
    x = 3
    def inni():
        y = 3
        result = x + y
        return result
    return inni

returnedVal = outi()
# print(returnedVal.__name__)
# x value is kept because outi returns a function and inni has x

# Decorators

def upper(func):
    def inner():
        str1= func()
        return str1.upper()
    return inner

# wraps function. takes function, sends it to upper function 
@upper
def greet():
    return "good afternoon"

# not needed with decorator
# greet = upper(greet)
print(greet())


def divByZero(func):
    def inner(x, y):
        if y == 0:
            return "divide by zero"
        return func(x, y)
    return inner

@divByZero
def div(x, y):
    return x / y

print(div(1,0))