# composition / aggregation
# is a / has a

# when you create a class, you are inheriting from an object: class Fish(object):
class Fish:
    def __init__(self, name, skele="bone", eyelids=False):
        self.__name = name
        self.__skele = skele
        self.__eyelids = eyelids

    def swim(self):
        print("Swimming")

    def swim_reverse(self):
        print("Swimming backwords")

# Trout extends fish
class Trout(Fish):
    pass


class Rectangle:
    def __init__(self, length, width=self.length):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    # overwriting
    def formatted_area(self):
        return f"{super().area()} cm^2" 


# multiple inheritance => may lead to disaster
# python mro 
class Crazy(Square, Fish):
    pass

# two problems with inheritance
# when child inherits from parent, it inherits everythong from parent (Python)
# child having multiple functionalities

class Person:
    def __init__(self, first_name, last_Name, learner=None, Teacher=None):
        pass

class Teacher:
    pass

class Learner:
    pass

armaan = Teacher("armaan")
armaan = Learner("armaan")

# composition
armaan = Person("first_name", "last_Name", Learner(), Teacher())