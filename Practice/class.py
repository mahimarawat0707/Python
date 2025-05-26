# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

  # Using 3 different parameter
class Students:
  def __init__(self, name, marks1, marks2, marks3):
    self.name = name
    self.marks1 = marks1
    self.marks2 = marks2
    self.marks3 = marks3

s1 = Students("Mahima", 99, 98, 100)
print(s1.name, s1.marks1, s1.marks2, s1.marks3)

  # Using list
class Students:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def get_avg(self):
    sum = 0
    for val in self.marks:
      sum += val
    print("HI!", self.name, "your avg marks is:", sum/3)

s1 = Students("Mahima", [99, 98, 100])
print(s1.name, s1.marks) 
s1.get_avg()

s1.name = "Ironman"
s1.get_avg()


#Create Account class with 2 attribute - balance & account no. Create method to debit, credit & printing the balance

class Account:
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance=", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance=", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(1000000, 235671893467)
acc1.debit(1000)
acc1.credit(908765)
acc1.credit(90000)