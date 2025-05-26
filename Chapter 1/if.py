G = input("m/f : ").lower()
A = float(input("A : "))
print("Fees is 1200\nChandigarh ---> Uttrakhand")
if G == "m" or "f":
  if 1<=A<=8:
    print("You can travel free of cost.")
elif G == "f" or "m":
  if 8<=A<=12:
    print("Half Fees")
elif G == "f" or "m":
  if A>=12:
    print("Full fees")
else:
  print("INVALID CREDINTAL...")