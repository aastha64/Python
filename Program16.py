#Tuple Program

DeptName =("HR", "Finance", "Learning", "Marketing", "IT", "Purchase")
newDept = list(DeptName)
newDept.append("Payroll")
DeptName = tuple(newDept)
print(DeptName)


visitors = ["John", "Sergei", "Anshul", "Irfaan", "Pooja", "Sakshi", "Jatin", "Sergei", "Saroj", "Jatin"]
UinqueVisitors = set(visitors)
print(UinqueVisitors)