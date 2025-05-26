""" *
    * *
    * * *
    * * * *
    * * * * * """

n = int(input("Enter a number: "))
print(n)
for i in range(1, n+1):
  print("*"*i)

"""    *
      ***
     *****
    *******
   ********* """
n = int(input("Enter a number: "))
print(n)
for i in range(1, n+1):
  print(" "*(n-i)+"*"*(2*i-1))

""" ***** 
    *   *
    *   *
    *****  """
def print_star_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()  
n = 3
print_star_pattern(n)
