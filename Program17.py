# Other Operations on Set
pricorus=("Sales", "IT", "CSO", "FSO", "LOM")
symphony=("Sales", "CSO", "Purchase", "BR", "Admin")

#symphony has procured pricorous
newdepts= pricorus-symphony  #findinf the difference
print("New Depts To Be Formed")
print(newdepts)
print("Total New Depts = "(len (newdepts)))

cdept=pricorus & symphony  # 
print("Common Depts To Be Formed")
print (cdept)
print("Total Common Depts = "(len (cdept)))
alldepts=symphony | pricorus
print("Overall Depts Are")
print(alldepts)
print("Total Depts=id" ,len (alldepts))