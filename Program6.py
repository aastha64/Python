# Input a number and check if it is divisible by both 5 and 8
choice  = "y"
while choice == "y" or choice == "Y":
    num = int(input("Enter the number: "))
    if num % 5 == 0 and num % 8 == 0:
        print ("Divisible by both 5 and 8")
    elif num % 5 == 0 and num % 8 != 0:
        print ("Divisible by 5 but not by 8") 
    elif num % 5 != 0 and num % 8 == 0:
        print ("Divisible by 8 but not by 5") 
    elif num % 5 != 0 and num % 8 != 0:
        print ("Neither divisible by 5 nor by 8") 

    if choice == "y" or choice == "Y":
        continue
    else:
        break


