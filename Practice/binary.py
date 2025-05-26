#Convert Decimal number to Binary number
print("1. Decimal to Binary Convertor")
def binary(num):
  if num > 1:
    binary(num//2)
  print(num%2, end="")
 
num = int(input("Enter a decimal number: "))
binary(num)
print()
print()

#Addition and Subtraction of Binary numbers
print("2. Addition and Subtraction")
def binary1(num1):
  if num1 > 1:
    binary1(num1//2)
  print (num1%2, end="")

def binary2(num2):
  if num2 > 1:
    binary2(num2//2)
  print (num2%2, end="")

def binary3(sum):
  if sum > 1:
    binary3(sum//2)
  print (sum%2, end="")

def binary4(diff):
  if diff >0:  
    if diff > 1:
      binary4(diff//2)
    print(diff%2, end="")
  else:
    print("Difference is in negative.")

num1 = int(input("Enter a decimal number: "))
num2 = int(input("Enter a decimal number: "))
sum = num1 + num2
diff = num1 - num2
print(f"Binary of {num1} is:-")
binary1(num1)
print()
print()

print(f"Binary of {num2} is:-")
binary2(num2)
print()
print()

print(f"{num1} + {num2} = {sum}. Binary of {sum} is :-")
binary3(sum)
print()
print()

if diff >= 0:
  print(f"{num1} - {num2} = {diff}. Binary of {diff} is :-")
binary4(diff)
print()
print()

#Convert Binary Number into decimal
print("3. Binary to Decimal Convertor")
binary= input("Enter a binary number: ")
a = 0
for i in binary:
  a = a*2 + int(i)
print(f"Decimal of {binary} is {a}")