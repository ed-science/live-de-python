from collections import UserString


class MyString(UserString):
    def __iter__(self):
        return iter(self.data)

    def next(self):
        yield from self.data
