list = ["A", "B", "C", "D", "E"]
m = 1
for num in list:
  print(f" {m}- {num}")
  m += 1

#__________________________________________________________
name = input("Enter your name... ")                       #|
print(name.title()) #capitalize every first word          #|
#__________________________________________________________|


list = ["A", "B", "C", "D", "E"]
for idx, num in enumerate(list, 1):
  print(f"{idx}: {num}")

#_________________
a = {}           #|
print(type(a))   #|
#_________________|

#_________________
a = set()        #|
print(type(a))   #|
#_________________|