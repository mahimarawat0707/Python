#constructor :All classes havee a function called __init__(), which is always executed when the class is being initiated.

class Student:
  college_name = "ABC College" #Class Attribute
  name = "anonymous"

  #Default constructors
  def __init__(self):
    pass

  #parameterized constructors
  def __init__(self, name, marks): #The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    self.name = name  #obj attribute > class attribute
    self.marks = marks 
    print("Adding new student in database")

s1 = Student("Nina Petrova", 97) #instance attribute
print(s1.name, s1.marks)

s2 = Student("Aaron Russo", 89) #instance attribute
print(s2.name, s2.marks)

print(s2.college_name)
print(Student.college_name) #same output
