class EmobilisStudent:
  def __init__(self, name, age):
    self.name=name
    self.age=age
  def hello_me(self):
    print(f"My name is {self.name} and im {self.age} years old.")

class Schoolroll:
  def __init__(self, name, year):
    self.name=name
    self.year=year
  def instituition_info(self):
      print(f"My school is called {self.name} and it was started in {self.year}")

class Magari:
  def __init__(self, model, make, year):
    self.model=model
    self.make=make
    self.year=year
  def company_info(self):
    print(f"this car is a {self.model} model of make {self.make} and it was manufactured in {self.year}")

class rockets:
  def __init__(elon, company, model, booster):
    elon.comapany=company
    elon.model=model
    elon.boosters=booster
  def boosters_type(elon):
    print(f"This rocket is developed by {elon.comapany} and is a {elon.model}. It is powered by {elon.boosters} boosters")

class books:
  def __init__(vitabu, title, pages, author):
    vitabu.title=title
    vitabu.pages=pages
    vitabu.author=author
  def bookz_type(vitabu):
    print(f"This book is writen by {vitabu.author} and is called {vitabu.title}. It is a {vitabu.pages} page book")
#creating an object
myobj=EmobilisStudent("Solomon", 19)
myobj.hello_me()

myobj=Schoolroll("nyeri high", 1923)
myobj.instituition_info()

carobj=Magari("mercedes", "G-wagon", 2022)
carobj.company_info()
carobj=Magari("toyota", "supra", 2019)
carobj.company_info()
carobj=Magari("ford", "Gt", 1999)
carobj.company_info()
carobj=Magari("bmw", "x6", 2020)
carobj.company_info()
carobj=Magari("tesla", "model x", 2017)
carobj.company_info()

rockobj=rockets("Spacex", "Starship", "Falcon heavy")
rockobj.boosters_type()

bookzobj=books("Will Robie", 403, "David Baldacci")
bookzobj.bookz_type()

