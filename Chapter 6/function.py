#function definition
def calc_sum(a, b): #(parameter)
  sum = a + b
  print(sum)
  return sum
calc_sum(13, 56) #(argument); function call


def calc_dif(a, b):
  dif = a - b
  print(dif)
  return dif
calc_dif(45, 12) 

def cal_prod(a= 4, b=2):
  print(a * b)
  return a * b
a = 5
cal_prod () #if we will not put any value in it. It will take the above value as by default

#Print Hello
def print_hello():
  print("Hello!!!")
 
print_hello()

#AVERAGE OF 3 NUMBERS
def average(a, b, c):
  avg = (a+b+c)/3
  print(avg)
  return avg
average(2,4,3)

#print function
print("Mahima","Rawat") #sep = " "
print("Mahima", end="$")#end = "\n"
print("Rawat")