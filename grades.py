grade=float(input("Enter your grade :"))
if grade>=90 and grade<=100:
  print("You got an A")
elif grade>=70 and grade<=89:
  print("You got a B+")
elif grade>=60 and grade<=69:
  print("You got a B")
elif grade>=50 and grade<=59:
  print("You got a B-")
elif grade>=40 and grade<=49:
  print("You got a C+")
elif grade>=30 and grade<=39:
  print("You got a B")
elif grade>=20 and grade<=29:
  print("You got a C-")
elif grade>=10 and grade<=19:
  print("You got a D")
elif grade>=1 and grade<=9:
  print("You got a E")  
else:
  print("Wrong input")

