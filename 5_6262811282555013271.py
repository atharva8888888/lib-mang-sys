# Library Management System
class Library:
    users={"suyog":["123","suyog@gmail.com"]}
    def __init__(self):
        self.ObooksList = {"Coding":["python","datastructure","c","core java","testing"],"History":["shreeman yogi","swami vivekanand","krishnaniti","pavankhind","prakash vata"],"Humour":["pune ek sathvan","batatychichal","vakroti"],"Sports":["driven:The Virat Kohli Story","captain cool","shuttler's flick"],"Poetry":["a poem a day","rumi","in other words","pluto"] } # list of books
        self.booksList = {"Coding":["python","datastructure","c","core java","testing"],"History":["shreeman yogi","swami vivekanand","krishnaniti","pavankhind","prakash vata"],"Humour":["pune ek sathvan","batatychichal","vakroti"],"Sports":["driven:The Virat Kohli Story","captain cool","shuttler's flick"],"Poetry":["a poem a day","rumi","in other words","pluto"] } # list of books
        self.name = "Knowledge"                                                               # library name
        self.BorrowDict = {}

    def regi(self):
        var=input("Enter your name to register : ")
        if var.isdigit():
            print("  x-x-x-x  print valid name  x-x-x-x  ")
        else:
            mail=input("Enter your E-mail :")
            if "@gmail.com" in mail: 
                if mail in self.users.get("suyog"):
                # if mail in self.users:
                    print("  x-x-x-x  This E-mail is already registered  x-x-x-x  ")   
                else:
                    password=input("Creat password : ")
                    self.users.update({var:[password,mail]})
                    # print(self.users)
                    print("your registration completed successfully.")
            else:
                print("  x-x-x-x  Enter valid E-mail  x-x-x-x  ")

    def librarian_login(self):
        self.var1=input("Enter your name : ")
        if self.var1=="librarian":
            password=input("Enter password : ")
            if password=="1234":
                print("----->| welcome librarian |<-----")     
                while(True):
                    print("....................")
                    print("\n1.DisplayBook \n2.AddBook \n3.DeleteBook  \n4.BorrowedBook \n5.Users  \n6:exit ")
                    print("....................")
                    choice2=input("Enter your choice : ")
                    if choice2=="1":
                        self.displayBooks()
                    elif choice2=="2":
                        self.addBook()
                    elif choice2=="3":
                        self.deleteBook()
                    elif choice2=="4":
                        if self.BorrowDict=={}:
                            print("No one borrowed a book")
                        else:
                            for i in self.BorrowDict.items():
                                print(i)
                    elif choice2=="5":
                        print("Users name :")
                        for i in self.users.keys():
                            print(i)
                    elif choice2=="6":
                        break
                    else:
                        print("  x-x-x-x  Enter valid choice  x-x-x-x  ")           
            else:
                print("  x-x-x-x  Incorrect Password  x-x-x-x  ")       
        else:
            print("  x-x-x-x  Enter valid name   x-x-x-x  ")

    def user_login(self):
        self.var2=input("Enter your name : ")             
        if self.var2 in self.users.keys():
            mail=input("Enter your E-mailid :")
            if "@gmail.com" in mail:
                if mail==self.users.get(self.var2)[1]:
                    password=input("Enter password : ")
                    if password==self.users.get(self.var2)[0]:
                        print("----->| Welcome",self.var2,"|<-----")
                        while(True):
                            print("....................")
                            print("1:DisplayBook  \n2:BorrowBook  \n3.ReturnBook \n4:exit ")
                            print("....................")
                            choice1=(input("Enter your choice : ") )
                            if choice1=="1":
                                self.displayBooks()
                            elif choice1=="2":
                                self.BorrowBook()
                            elif choice1=="3":
                                self.returnBook()  
                            elif choice1=="4":
                                print("Thenk you for visiting the library ")
                                break 
                            else:
                                print("  x-x-x-x  Enter valid choice  x-x-x-x   ")          
                    else:
                        print("  x-x-x-x  Incorrect Password   x-x-x-x  ") 
            else:
                print("  x-x-x-x  Enter valid E-mail  x-x-x-x  ")               
        else:
            print("  x-x-x-x  Enter valid name  x-x-x-x  ")

    def displayBooks(self):
        print("We have following Types of books in our library:")
        while(True):
            print("....................")
            print("1:coding  \n2:History \n3:Humour \n4:Sports  \n5:Poetry \n6.exit")
            print("....................")
            choice=input("Enter your choice :")
            if choice=="1":
                print("We have following books in our library:")
                for book in self.booksList.get("Coding"):
                    print("-->",book)
            elif choice=="2":
                print("We have following books in our library:")
                for book in self.booksList.get("History"):
                    print("-->",book)
            elif choice=="3":
                print("We have following books in our library:")
                for book in self.booksList.get("Humour"):
                    print("-->",book)
            elif choice=="4":
                print("We have following books in our library:")
                for book in self.booksList.get("Sports"):
                    print("-->",book)
            elif choice=="5":
                print("We have following books in our library:")
                for book in self.booksList.get("Poetry"):
                    print("-->",book)
            elif choice=="6":
                break
            else:
                print("  x-x-x-x  Enter valid choice  x-x-x-x  ")
           
    def BorrowBook(self):
        print("We have following books in our library:")
        while(True):
            print("....................")
            print("1:coding  \n2:History \n3:Humour \n4:Sports  \n5:Poetry \n6.exit")
            print("....................")
            choice=input("Enter your choice :")
            if choice in ["1","2","3","4","5","6"]:
                if choice=="1":
                    section="Coding"
                elif choice=="2":
                    section="History"
                elif choice=="3":
                    section="Humour"
                elif choice=="4":
                    section="Sports"            
                elif choice=="5":
                    section="Poetry"
                elif choice=="6":
                    break
                book=input("Enter book name : ")
                if book in self.booksList.get(section):
                    if book not in self.BorrowDict.keys():
                        self.BorrowDict.update({book:self.var2})
                        index=self.booksList.get(section).index(book)
                        self.booksList.get(section).pop(index)
                        print("You can take the",book,"book now")
                        # print(self.BorrowDict)
                    else:
                        print("Book is already being used.") 
                else:
                    print("  x-x-x-x  There is no book available with this name in ",section,"section  x-x-x-x  ")
            else:
                 print("  x-x-x-x  Enter valid choice  x-x-x-x  ")
                   
    def returnBook(self):
        print("We have following books in our library:")
        while(True):
            print("....................")
            print("1:coding  \n2:History \n3:Humour \n4:Sports  \n5:Poetry \n6.exit")
            print("....................")
            choice=input("Enter your choice :")
            if choice in ["1","2","3","4","5","6"]:
                if choice=="1":
                    section="Coding"
                elif choice=="2":
                    section="History"
                elif choice=="3":
                    section="Humour"
                elif choice=="4":
                    section="Sports"            
                elif choice=="5":
                    section="Poetry"
                elif choice=="6":
                    break
                book=input("Enter book name : ")
                if book in self.BorrowDict:
                    if book in self.ObooksList.get(section):
                        self.BorrowDict.pop(book)
                        self.booksList.get(section).append(book)
                        # print(self.BorrowDict)
                        # print(self.booksList.get(section))
                        print("your book has been returned suucefully ")
                    else:
                        print("  x-x-x-x  you can not return this book in these section  x-x-x-x  ")
                else:
                    print("  x-x-x-x In your BorrowedList there is no book with these name  x-x-x-x   ")
            else:
                print("  x-x-x-x  Enter valid choice  x-x-x-x  ")

    def addBook(self):
        print("We have following books in our library:")
        while(True):
            print("....................")
            print("1:coding  \n2:History \n3:Humour \n4:Sports  \n5:Poetry \n6.exit")
            print("....................")
            choice=input("Enter your choice :")
            if choice in ["1","2","3","4","5","6"]:
                if choice=="1":
                    section="Coding"
                elif choice=="2":
                    section="History"
                elif choice=="3":
                    section="Humour"
                elif choice=="4":
                    section="Sports"            
                elif choice=="5":
                    section="Poetry"
                elif choice=="6":
                    break 
                book=input("Enter book name : ")
                if book in self.booksList.get(section):
                    print("  x-x-x-x  Book is already exits  x-x-x-x  ")
                else:
                    self.booksList.get(section).append(book)
                    self.ObooksList.get(section).append(book)
                    print("Book has been added to the book list ")
                # for i in self.booksList.get(section):
                #     print("-->",i)
            else:
                print("  x-x-x-x  Enter valid choice  x-x-x-x  ")

    def deleteBook(self):
        print("We have following books in our library:")
        while(True):
            print("....................")
            print("1:coding  \n2:History \n3:Humour \n4:Sports  \n5:Poetry \n6.exit")
            print("....................")
            choice=input("Enter your choice :")
            if choice in ["1","2","3","4","5","6"]:
                if choice=="1":
                    section="Coding"
                elif choice=="2":
                    section="History"
                elif choice=="3":
                    section="Humour"
                elif choice=="4":
                    section="Sports"            
                elif choice=="5":
                    section="Poetry"
                elif choice=="6":
                    break
                book=input("Enter book name : ")
                if book in self.booksList.get(section):
                    index1=self.booksList.get(section).index(book)
                    self.booksList.get(section).pop(index1)
                    print("Book has been remove from the book list")
                    # print(self.booksList.get(section))
                else:
                    print("  x-x-x-x  There is no book with these name  x-x-x-x  ")
            else:
                print("  x-x-x-x  Enter valid choice  x-x-x-x  ")
                
    def home(self):
        print("\n----->|  Welcome to",self.name,"library  |<-----")
        while(True):
            print("....................")
            print("1:librarian_Login \n2:User_login \n3:Register \n4.exit")
            print("....................")
            choice=(input("Enter your choice : "))
            if choice=="1":
                self.librarian_login()    
            elif choice=="2":
                self.user_login()
            elif choice=="3":
                self.regi()
            elif choice=="4":
                break
            else:
                print("  x-x-x-x  Enter valid choice  x-x-x-x   ")
        
s=Library()
s.home()
