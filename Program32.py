# Creating Our Own Exception

class MyException(Exception):   # Exception is a predefined class in Python
    pass       # No Coding is required
class MyException1(Exception):
    pass

while True:
    try:
        empname=input("Enter Employee Name ").upper().strip()
            
        if( len(empname)==0):
            raise MyException1
        else:
            break
    except MyException1:   # Special Excepion Handler
        print("Name Can Not Be Blank Or It Should Not Contain any Digits")
        continue
    except:       # Default Exception Handler
        print("Some Other Exception")
        
while True:
    try :
        
        age=int(input("Enter Age "))
        if( age < 21 or age >=60):
            raise MyException # To raise the exception forcefully
            
        print("Employee Name = "+empname)
        print("Age of Employee =%d " %(age))
        break
    except ValueError:
        print("Improper Nos Entered...")
        continue
    except IOError:
        print("KeyBoard Failure Or Any Hardware Failure.....")
        continue
    except MyException:
        print("Age Can Not Be Less than 21 or >= 60")
        continue
    except :  # Default Exception Handler
        print("Sorry Exception Occured...")
        continue
    finally:
        print("Thanks")
print("Program Ended")

# exception handling
class emptynameexception(Exception):
    pass
class invalidnameexception(Exception):
    pass
class invalidemailidexception(Exception):
    pass
class invalidendwithemailidexception(Exception):
    pass
while True:
    try:
        name=input("Enter Name ")
        if(name=="" or name.isspace()):
            raise emptynameexception
        elif(name.isdigit()):
            raise invalidnameexception
        emailid=input("Enter Email Id ")
        pattern= "$akgec.ac.in"
        if not (emailid.endswith(pattern)):
            raise invalidendwithemailidexception
        if "@" not in emailid:
            raise invalidemailidexception
        print("Name = "+name)
        print("Email Id = "+emailid)
        break
    except emptynameexception:
        print("Name Can Not Be Blank")
    except invalidnameexception:
        print("Name Can Not Contain Digits")
    except invalidemailidexception:
        print("Email Id Should Contain @")
    except invalidendwithemailidexception:
        print("Email Id Should End With akgec.ac.in")
