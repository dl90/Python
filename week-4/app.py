class Person:

    # class variable
    # a variable that is shared among all instances of the class
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)
        self.title = title
        self.name = name
        self.surname = surname

    # instance method (method used on the object)
    # repr => representation method
    def __repr__(self):
        return self.name




steven = Person("Dr", "Steven", "Chao")
jeff = Person("Dr", "Jeff", "Lao")

print(steven)
print(jeff)

# can access calss variables from the instance
print(jeff.TITLES)
# -> Person.TITLES
# if fetching class variable
print(Person.TITLES)


class Berson:
    # class variable
    deceased = False

    def mark_as_deceased(self):
        # instance variable set
        self.deceased = True

personA = Berson()
print(personA.deceased) # Person.deceased
# python looks for instance variable first then class variable
personA.mark_as_deceased()
print(personA.deceased) # personA.deceased


class herson:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet): # instance method, self
        self.pets.append(pet) # Person.pets


jo = herson()
blo = herson()

jo.add_pet("dog")
print(jo.pets)
print(blo.pets)


# Person. ___ -> class variable / class method
# cls -> refers to the class