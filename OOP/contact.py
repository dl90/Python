import datetime as dayTime

class ContactCard:
    def __init__(self, _name, _surname, _birthday, _address, _phone, _email):
        self.name = str(_name)
        self.surname = str(_surname)
        self.birthday = dayTime.datetime.strptime(_birthday, '%b %d, %Y')
        self.address = str(_address)
        self.phone = int(_phone)
        self.email = str(_email)

    def age(self):
        if hasattr(self, "_age"):
            return self._age

        # age = (dayTime.datetime.today() - self.birthday)
        # print(age)
        today = dayTime.datetime.today()
        age = today.year - self.birthday.year
        return age

        # if (today < dayTime.date(self.birthday.year, self.birthday.month, self,birthday.date)):
        #     age = age - 1

        #     self._age = age
        #     return age


John = ContactCard("John", "A", "Jan 20, 2000", "123 abc street", 1233211234, "John@abc.ca")
print(John.age())