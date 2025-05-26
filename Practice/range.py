#Print number from 1 to 100.
for i in range(1, 101):
  print(i)

#Print number from 100 to 1.
for i in range(100, 0, -1):
  print(i)

#Print the multiplication table of a number n.
num = int(input("Enter a number"))
for i in range(1,11):
  print(num*i)

#WAP to find the sum of first natural numbers. 
n = 9 
sum = 0
for i in range(1, n+1):
  sum += i
print("Total sum is", sum)
  
"""using While Loop"""
n = 7
sum = 0
i = 1
while i <= n:
  sum += i
  i +=1
  print("Total sum is", sum)

#WAP to find the factorial of the first n numbers.
n = 3
fact = 1
i = 1
while i <= n:
  fact *= i
  i += 1
  print("Total factorial is", fact)

"""Using For Loop"""
n = 5
fact = 1

for i in range(1, n+1):
  fact *= i
print("factorial =", fact)