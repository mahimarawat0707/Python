i = 1
while i <= 5:
  print(i)
  if(i == 3):
    break
  i += 1
print("End of loop")

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(nums):
  if(nums[i] == x):
    print("Fount at idx", i)
    break
  else:
    print("FINDING...")
  i += 1

#CONTINUE
i = 0
while i <= 5:
  if(i == 3):
    i += 1
    continue 
  print(i)
  i += 1