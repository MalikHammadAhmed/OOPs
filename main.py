# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Parent Class or Base Class
class Person(object):
    def __init__(self, name, idnumber):
        self.__name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My idnumber is {}".format(self.idnumber))

#Child Class or Inherit Class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        #invoking the constructor of parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}" .format(self.name))
        print("Idnumber is {}" .format(self.idnumber))
        print("Post: {}" .format(self.post))

a = Employee('Rahul', 12345, 12000, 'ML Engineer')

a.display()
a.details()


