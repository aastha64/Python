#Example of various dictionary functions
import pandas as pd
mydict = {"PR01":("Automizing IT Section",16,56) , "PR71":("Budget Planning",10,7), "PR21":("SAP Implementation",16,50)}
mydict2 = {"PR29":("AOnline Trainig",5,30), "PR32":("PF Updation",5,7)}
mydict.update(mydict)
projectcode = input("Enter project code").upper()
if(projectcode in mydict.keys()):
    print(str(projectcode) + "\t\t", mydict.get(projectcode))
else:
    print("This project does not exist")

# Now identify which project has max man power
manpower=[]
for x in mydict:
    manpower.append(mydict.get(x)[2])
print("Maximum manpower is:", max(manpower))
print("List of all projects")
items = pd.DataFrame(mydict)
print(items)