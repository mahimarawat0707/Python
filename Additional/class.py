class Person:
  name = "Mahima"
  occupation = "Software Developer"
  networth = 100000000000000
  def info(self): #self= The method that is being called on this object
    print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
a.name = "Rajat"
a.occupation = "Accountant"
# print(a.name, a.occupation)

b.name = "Nitika"
b.occupation = "HR"
b.info()