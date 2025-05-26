# Abstraction- Hinding the implementation detail of a class and only showing the essential features to the user.
class Car:
  def __init__(self):
    self.acc = False
    self.brk = False
    self.clutch = False

  def start(self):
    self.clutch = True
    self.acc = True
    print("Car started")

car1 = Car()
car1.start()

# Encapsulation- Wrapping data and function into a single unit (object).

