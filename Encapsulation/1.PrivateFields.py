class Student:
    def __init__(self):
        self.__id = 100
        # by using __ (double underScore we can mark a field as private
        self.__name = "suhail"

    def display(self):
        print(self.__id)
        print(self.__name)

s=Student()
# print(s.id)
# print(s.name)
# we can access private field with name mangling
print(s._Student__id)