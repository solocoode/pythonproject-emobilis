#list in python
myclassmate=["Erick","Joan","Micheal","Victor"]
mynos=[3,7,9,2,6,0,8]
mynos.sort()
myclassmate[0]="solo"
myclassmate.append("daniel")
myclassmate.insert(2, "christine")
myclassmate.insert(0, "obienji")
print(mynos)
#myclassmate.sort()
print(myclassmate)
print("Her name is "+ myclassmate[1])
print("His name is "+ myclassmate[0])
print("His name is "+ myclassmate[2])
print("His name is "+ myclassmate[3])
print("His name is "+ myclassmate[4])

#tuple in python
myfavfruits=("mangoes","apples","apples","pineapples","oranges")
print(myfavfruits)
#myfavfruits.__add__("banana")
print(myfavfruits[0])

#set datastructure(unorganised)
myfavcars={"toyota","pagani","koeniseg","tesla","nissan","mercedes"}
myfavcars.add("buggati")
print(myfavcars)

#dictionaries in python
magari={
  "Name":"Toyota",
  "Model":"Premio",
  "Year of manufacture":"2020"
}
print(magari)
print(magari["Model"])
