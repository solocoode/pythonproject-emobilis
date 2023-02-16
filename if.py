x=1
marks=67
grades=90
#if statement
if x>0:
  print("The number is positive")
  print(4+10)
#if else statement
if marks>=60:
  print("You have passed")
else:
  print("You have failed")
#if....elif.......else
if grades<=29 and grades>=0:
  print("You have failed")
elif grades<=49 and grades>=30:
  print("You have passed")
elif grades<=79 and grades>=50:
  print("You have credit")
elif grades<=100 and grades>=80:
  print("You have distinction")
else:
  print("Wrong input")

#my example of if statments
amount=int(input("What are your funds  worth :"))
if amount<=100 and amount>=0:
  print("You have insufficient funds")
elif amount<=200 and amount>=101:
  print("You have just enough funds")
elif amount<=300 and amount>=201:
  print("You have enough funds")
elif amount<=1000 and amount>=500:
  print("You have more than enough funds")
elif amount<=10000 and amount>=1001:
  print("You have unlimited resources")
else:
  print("Wrong input")
