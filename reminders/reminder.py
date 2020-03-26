
class Reminder:

    def __init__(self, tag, reminder_):
        self.__tag = [tag]
        self.__reminder = reminder_

    def __repr__(self):
        return self.reminder

    @classmethod
    def strip(cls, arg):
        return arg.strip()

    @property
    def reminder(self):
        return self.__reminder

    @reminder.setter
    def reminder(self, input):
        _input = Reminder.strip(input)
        if(len(_input) > 0):
            self.__reminder = _input
        else:
            self.__reminder = None

    @property
    def tag(self):
        return " ".join(self.__tag)

    @tag.setter
    def tag(self, tag):
        _tag = Reminder.strip(tag)
        if len(_tag) > 0:
            tags = _tag.split(",")
            self.__tag = map(lambda x: Reminder.strip(x), tags)
        else:
            self.__tag = None
