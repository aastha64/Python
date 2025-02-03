# Lab Question
choice = "Y"

while True:
    employee_name = input("Enter Employee Name: ").upper().strip()
    if len(employee_name) == 0:
        print("Blank name not allowed....Re Enter..")
        continue
    salary = float(input("Enter Salary: "))
    if salary < 25000:
        print("It is Not a Valid Salary. Enter a Correct Value.")
        continue
    email = input("Enter Email ID:").lower().strip()
    if len(email) == 0:
        print("Email ID cannot br blank")
        continue    
    print("NAME\t\t\tSALARY\t\Email ID")
    print("****\t\t\t******\t\t*******")
    print("%s\t\tRs  %.2f\t\t%s" %(employee_name, salary,email))

    choice = input("Want to generate enother salary slip? ").upper().strip()
    if choice == "Y":
        continue
    else:
        break
print("Program Ended")