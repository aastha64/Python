# example of dictionary
mydict = {1004:("Nidhi", "CSE","A"), 1012:("Saurav", "ME"), 1198:("Aastha", "CSE","A"), 1501:("Saurav", "CSE", "B")}

mydict2 = {1019:("Vikas","ECE","A"), 1214:("Tanu", "CSE", "A")}
mydict.update(mydict2) # used for combining one dictionary with other
flag = 0
print(mydict)
print("Roll No\t\tcourse\tgrade")

for x in sorted(mydict.keys()): # will print all the key and values as mentioned
    print(str(x) + "\t" +str(mydict.get(x)))

for x in sorted(mydict.keys()): # will sort the output in ascending key order
    print(str(x) + "\t" +str(mydict.get(x)))

for x in sorted(mydict.keys(), reverse = True): #will sort the output in descending key order
    print(str(x) + "\t" +str(mydict.get(x)))

print("Total students = %d" %len(mydict))          
cname = input("Enter the name :") .strip().upper()
for x in sorted(mydict.keys()):
    record = list(mydict.get(x))
    sname=  record[0].upper()
    if (sname == cname):
        print("Record Found")
        print(str(x)+"\t"+str(mydict.get(x)))
        flag = 1
    if(flag == 0):
        print("Record Not Found")
del(flag,record) #used tp remove any object from memory