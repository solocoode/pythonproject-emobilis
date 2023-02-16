#function is a block of code that executes code
def hello():
  print("This is my first function")
hello()

def calculate( x=12, y=45):
  print(x*y)
calculate()
#functions with variiables
def majina(fname, lname):
  print(fname+ " "+ lname)
majina("solomon", "njogo")
majina("stephen", "thuita")
majina("susan", "muthoni")
#functions with an argument
def greetings(name, greetings="hello"):
  print(greetings+ " "+ name)
greetings("solomon")
greetings("niaje", "solo")
greetings("solo", "niaje")
#functions with an argument
def gari(model, company="Tesla"):
  print(company+ " "+model)
gari("model s")
gari("model 3")
gari("model x")
gari("model y")
#return the maximum value in data
def maxvalue(a, b, c, d, e, f):
  return max(a, b, c, d, e, f)
result=maxvalue(7,9,1,8,17,45)
print(result)

#return the minimum value in data
def minvalue(a, b, c, d, e, f):
  return min(a, b, c, d, e, f)
result=minvalue(99,45,12,89,5,1)
print(result)
#function that sorts
def sort_list(lst):
  return sorted(lst)
answer=sort_list([3,9,0,2,7,11,5,5,4,2])
print(answer)
#function that prints out numbers
def print_numbers(n):
  for i in range(n):
    print(i)
print_numbers(5)
