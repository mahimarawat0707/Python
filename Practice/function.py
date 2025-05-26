#WAF to print the length of a list. (list is the parameter)
num = [1,2,3,4,5]
heroes = ["Thor", "Ironman", "Captain America", "Scarlet Witch", "Hulk"]
def list(list):
  print(len(list))
list(num)
list(heroes)

#WAF to print the elements of a list in a single line.
num = [1,2,3,4,5]
heroes = ["Thor", "Ironman", "Captain America", "Scarlet Witch", "Hulk"]
def list(list):
    for items in list:
      print(items, end=", ")
list(heroes)
print()

#WAF to find the factorial of n. (n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(9)

#WAF to convert USD to INR
def cov_mon(USD):
  INR = USD * 85
  """print(USD, "USD =", INR, "INR")
  print(INR)"""
  return INR
con=cov_mon(100) 
print(con)

#WAF to wish happy birthday
def happy_birthday(name, age):
   print(f"Happy Birthday to {name}!")
   print(f"You are {age} years old!")
   print("Happy birthday to you!")
   print()

happy_birthday("Bro", 20)
happy_birthday("Steve", 30)
happy_birthday("Joe", 40)

def display_invoice(username, amount, due_date):
   print(f"Hello {username}")
   print(f"Your bill of ${amount} is due: {due_date}")
display_invoice("BroCode", 42.50, "01/01")   


def create_name(first, last):
   first = first.capitalize()
   last = last.capitalize()
   return first +  " " + last
create_name("Mahima", "Rawat")