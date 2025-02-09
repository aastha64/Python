# Class & Objects
import os


class Book:
    def _init_(myobj):
        myobj.publisher = "Penguine"
    def EnterBookDetail(myobj):
        myobj.BookName=input("Enter Book Name ").strip().title()
        myobj.AuthorName=input("Enter Author Name ").strip().title()
        myobj.price=int(input("Enter Price "))
        myobj.publisher=input("Enter Publisher Name ").strip().title()
    
    def ShowGreetings(m1):
        print("Welcome to our bookstore")

    def ShowBookDetail(myobj):
        heading="List of Books"
        print(heading)
        print("Book Name =",myobj.BookName)
        print("Author Name =", myobj.AuthorName)
        print("Price =%.2f" %myobj.price)
        print("Publisher =",myobj.publisher)

    def StoreFile(myobj):
        fv = open(":E:\\ Akgec\\BookList.csv", "a") # w for write mode ehere old entries will be overwritten
                                                    # r for reading 
                                                    # a for appending
        data = myobj.BookName+ "," +myobj.AuthorName+ " , " +str(myobj.price)+ "," +myobj.publisher
        fv.write(data) #closing the file
        fv.close()
        print("Recored Added")
    def ReadFile(myobj):
        fv = open(":E:\\ Akgec\\BookList.csv", "r")
        data = fv.read()
        print(data)
        lines = data.split("\n")
        print("Total Records = %d" %(len(lines)-1))
        size = os.path.getsize(":E:\\ Akgec\\BookList.csv")
        print("Actual File Size =" , size)
        fv.close()
    
book1=Book()  # Creating an object 
book1.ShowGreetings()
book1.EnterBookDetail() # Book.EnterDetail(book1)
book1.ShowBookDetail()  # Book.ShowDetail(book1)
book1.StoreFile()
book2 = Book("BPB")
book2.EnterBookDetail()
book2.ShowBookDetail()
book2.StoreFile()
del book1,book2

# Now add another functionality say ReadFile() so that we can see the -
# file content and count no. of records, also the size of te file