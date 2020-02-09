class Bookstore:

    def __init__(self, store_name):
        self.name = store_name
        self.inventory = []

    def addBook(self, book):
        repr(type(book))
        if type(book) == type(Book):
            print("yes")
        self.inventory.append(book)
        print(f"{book.title} + added")

    def getBook(self, book):
        for b in self.inventory:
            if b == book:
                return book
            else:
                return None

    def getBooks(self):
        return self.inventory

    def searchBooks(self, title):
        for b in self.inventory:
            if b.title == title:
                return b
            else:
                return None

    def searchByAuthor(self, lastname):
        arr = []
        for b in self.inventory:
            if b.author.lastname == lastname:
                arr.append(b)
        return arr

    def searchByTitleAndAuthor(self, title, lastname):
        for b in self.inventory:
            print(b.author.lastname)
            if b.title == title and b.author.lastname == lastname:
                return b
            else:
                return None

    def superSearch(self, title=None, author=None):
        if title == None and author == None:
            return "No search params supplied"
        elif author == None:
            arr = []
            for b in self.inventory:
                if b.title == title:
                    arr.append(b)
            return arr
        elif title == None:
            arr = []
            for b in self.inventory:
                if b.author.lastname == author.lastname:
                    arr.append(b)
            return arr
        else:
            arr = []
            for b in self.inventory:
                if b.title == title and b.author.lastname == author.lastname:
                    arr.append(b)
            return arr


class Book:

    def __init__(self, name, author, year, language, isbn):
        self.title = name
        self.author = author
        self.year = year
        self.language = language
        self.isbn = isbn

class Author:

    def __init__(self, firstname, lastname, nationality=None, active=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nationality = nationality
        self.active = active
        self.booksWritten = []

    def addToBooksWritten(self, book):
        self.booksWritten.append(book)

    def removeBooksWirtten(self, book):
        self.booksWritten.remove(book)


Bob = Author("Bob", "Smith", "US", True)
Poe = Author("Edgar Allan", "Poe", "US", False)

BobsBook = Book("Bob's Book", Bob, 2000, "English", "123123123")
BobsBook1 = Book("Bob's Book1", Bob, 2001, "English", "2132323232")
BobsBook2 = Book("Bob's Book2", Bob, 2002, "English", "32131232")
PoeBook = Book("raven", Poe, 1234, "English", "178234878712")

Bob.addToBooksWritten(BobsBook)
Bob.addToBooksWritten(BobsBook1)
Bob.addToBooksWritten(BobsBook2)

Bob.removeBooksWirtten(BobsBook2)

for book in Bob.booksWritten:
    print(book.title)


myStore = Bookstore("myBookStore")

print(myStore.name)

myStore.addBook(BobsBook)
myStore.addBook(BobsBook1)
myStore.addBook(BobsBook2)
myStore.addBook(PoeBook)

print("--get all books--")
booksInStore = myStore.getBooks()
for book in booksInStore:
    print(book.title)

print("--search--")
searchedBook = myStore.searchBooks("Bob's Book")
print(searchedBook.title)

print("--search by author--")
searchAuthorBook = myStore.searchByAuthor("Smith")
for x in searchAuthorBook:
    print(x.title)

print("--search by title and author--")
searchTitleAndAuthor = myStore.searchByTitleAndAuthor("Bob's Book2", "Smith")
print(searchTitleAndAuthor)


print("--superSearch title--")
# Searching *just* by title:
result1 = myStore.superSearch(title="Bob's Book")
if len(result1) > 0:
    for x in result1:
        print(x.title)
else:
    print("no results")


print("--superSearch author--")
# Searching *just* by author:
poe = Author(firstname='Edgar Allan', lastname="Poe", nationality='US')
result2 = myStore.superSearch(author=poe)
if len(result2) > 0:
    for x in result2:
        print(x.title)
else:
    print("no results")


print("--superSearch title && author--")
# Searching by both title *and* author:
poe = Author(firstname='Edgar Allan', lastname="Poe", nationality='US')
result3 = myStore.superSearch(title='raven', author=poe)
if len(result3) > 0:
    for x in result2:
        print(x.title)
else:
    print("no results")