# List Related Programs
# List is a collection of objects seperated by comma and also enclosed by a pair of square brackets
# List can be empty
# List can have multiple values of multiple datatypes
# Most flexible data type in python

techcourse = ["Python", "Oracle", "AWS", "Cyber Security", "Java", "Linux"]
ecourse = ["Soft Skills", "German", "PMP", "Customer Finding", "Resume Building"]
allcourse = techcourse + ecourse

allcourse.remove("Cyber Security")
allcourse.insert(1, "Big Data") # To add an item at a specific position
allcourse.sort() # sorting is ascending order
allcourse.append("Excel") # inserting an element from last
allcourse.append("MySQL")
allcourse.append("Jira")
allcourse.pop()# it will remove the element from last
allcourse.pop(5) # it will remove the element at a particular index  
print("List of all courses: ")
for x in allcourse:
    print(x) #it will print all courses in sequential order
print("Total Cousres = ", len(allcourse))
cname = input("Course name to search ?").strip().upper()
newList = [] # a blank list
for x in allcourse:
    cname.append(x.upper())
if cname in newList:
    print("%s is available" %cname)
else:
    print("%s is not available" %cname)