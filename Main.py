class library:
    books_list=['DSA','Python-Basics','Deep learning','Neural Networks','Tensorflow','Python-Advanced','Excel-basics','Graphs(Ed-2)','Statistics']
    
    def display_books(self):
        print("--List of Books--\n")
        for book in self.books_list:
            print(f"~ {book}")
    
    def issue_book(self,bookname):
        if bookname in self.books_list:
            self.books_list.remove(bookname)
            print(f"~The book: {bookname} Has been Issued~")
        else:
            print("Error !Specified book is not present in a library!")
    
    def add_book(self,bookname):
        self.books_list.append(bookname)
        print('~Book is returned successfully~')

class student:
    req_book=''
    ret_book=''
    def request_book(self):
       self.req_book=input("Enter the Book name You want to issue: ")
       return self.req_book
    
    def return_book(self):
       self.ret_book=input("Enter the Book name You want to Return: ")
       return self.ret_book
   
##Start of main Program

college_library=library()
college_student=student()
print('#######################')
print('### COLLEGE LIBRARY ###')
print('#######################\n')
print('~~~Options')
print('1.Display books')
print('2.Request book')
print('3.Return book')
print('4.Exit')

while 1==1:

    choice=int(input("Enter Your choice: \n"))

    if   choice==1: college_library.display_books()
    elif choice==2: college_library.issue_book(college_student.request_book())
    elif choice==3: college_library.add_book(college_student.return_book())
    elif choice==4:exit(0)










        

    
    
    
        
        

                
        

    
    
    




