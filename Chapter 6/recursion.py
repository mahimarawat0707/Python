#function calling itself
import sys 
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i = 0
def greet(): 
  global i
  i += 1
  print("Hello", i)
  greet()
greet()


def show (n):
  if(n == 0):
    return
  print(n)
  show(n-1)
  print("END")
  

show(5)

#Factorial
def fact(n):
  if(n == 1 or n == 0):
    return 1
  return fact(n-1) * n
print(fact(9))