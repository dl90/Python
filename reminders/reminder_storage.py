

class ReminderStorage:
    
    def __init__(self):
        self.__storage = []

    def __repr__(self):
        return str(self.__storage)

    @property
    def storage(self):
        return self.__storage

    @storage.setter
    def storage(self, arg):
        self.__storage = arg

    def append(self, item_):
        self.__storage.append(item_)

    def insert(self, item_):
        self.__storage.insert(item_)

    def extend(self, list_):
        self.__storage.extend(list_)
