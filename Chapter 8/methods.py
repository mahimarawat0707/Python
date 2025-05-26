#Methods are basically function that belong to object
class Student:

  def __init__(self, name, marks):
    self.name = name
    self.marks = marks 

  def welcome(self):
    print("Welcome student,", self.name)

  def get_marks(self):
    return self.marks

s1 = Student("Nina Petrova", 97)
s1.welcome()
print(s1.get_marks())

