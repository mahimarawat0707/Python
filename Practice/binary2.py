class binary_number:
    def __init__(self, num1, num2=0):
        self.num1 = num1
        self.num2 = num2

    def decimal_to_binary(self):
        lst = []
        if self.num1 == 0:
            print("zero in binary is 0") 
        num = self.num1
        while num > 0:
            remainder = num % 2
            lst.append(str(remainder))
            num = num // 2
        lst.reverse()
        print(f"{self.num1} in binary is ",''.join(lst))

    def sum_of_number(self):
        lst1 = []
        n1 = self.num1
        if n1 == 0:
            print("zero in binary is 0")
        else:
            while n1 > 0:
                rem = n1 % 2
                lst1.append(str(rem))
                n1 = n1 // 2
            lst1.reverse()
            print(f'{self.num1} in Binary is :', ''.join(lst1))

        lst2 = []
        n2 = self.num2
        if n2 == 0:
            print("zero in binary is 0")
        else:
            while n2 > 0:
                rem = n2 % 2
                lst2.append(str(rem))
                n2 = n2 // 2
            lst2.reverse()
            print(f'{self.num2} in Binary is :', ''.join(lst2))

        total = self.num1 + self.num2
        lst3 = []
        if total == 0:
            print("zero in binary is 0")
        else:
            while total > 0:
                rem = total % 2
                lst3.append(str(rem))
                total = total // 2
            lst3.reverse()
            print(f'Sum({self.num1 + self.num2}) Binary:', ''.join(lst3))
    def diff_of_number(self):
        lst1 = []
        n1 = self.num1
        if n1 == 0:
            print("zero in binary is 0")
        else:
            while n1 > 0:
                rem = n1 % 2
                lst1.append(str(rem))
                n1 = n1 // 2
            lst1.reverse()
            print(f'{self.num1} in Binary is ', ''.join(lst1))

        lst2 = []
        n2 = self.num2
        if n2 == 0:
            print("zero in binary is 0")
        else:
            while n2 > 0:
                rem = n2 % 2
                lst2.append(str(rem))
                n2 = n2 // 2
            lst2.reverse()
            print(f'{self.num2} in Binary is ', ''.join(lst2))

        diff = self.num1 - self.num2
        lst3 = []
        if diff == 0:
            print("zero in binary is 0")
        else:
            while diff > 0:
                rem = diff % 2
                lst3.append(str(rem))
                diff = diff // 2
            lst3.reverse()
            print(f'diff({self.num1 - self.num2}) Binary:', ''.join(lst3))
    def binary_to_decimal(self):
        if self.num1 ==0:
            print("zero in binary is 0")
            return
        o = 0
        decimal = 0
        m = str(self.num1)
        for i in reversed(m):
            decimal += int(i)*(2**o)
            o +=1
        print(f"{self.num1} in decimal is : {decimal}")

while True:
  print("--Information--\ndecimal_to_binary-->(c)\nbinary_to_decimal-->(ct)\naddition-->(a)\nsubstraction-->(s)")
  choice = input("Enter :- ").lower().strip()#.strip()- to remove the gappings

  if choice == "c":
      num1 = int(input("what is your number :"))
      obj = binary_number(num1)
      obj.decimal_to_binary()
  elif choice == "a":
      num1 = int(input("what is your first number :"))
      num2 = int(input("what is your second number :"))
      obj = binary_number(num1, num2)
      obj.sum_of_number()
  elif choice == "s":
      num1 = int(input("what is your first number :"))
      num2 = int(input("what is your second number :"))
      f = num1 - num2 
      if f >=0:
          obj = binary_number(num1, num2)
          obj.diff_of_number()
      else :
          print ("Negative value !404")
  elif choice == "ct":
      num1 = int(input("what is your binary number :"))
      obj = binary_number(num1)
      obj.binary_to_decimal()
  else:
      print("Invalid Error ! Try again :))")
      continue
  while True:
    mood = input("Enter to continue and 'n' to Exit :").lower().strip()
    if mood == "":
      break
    elif mood == "n":
      print ("Thanks")
      quit()
    else:
      print("olny enter and 'n'")