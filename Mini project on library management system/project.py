class Library:
    def __init__(self, book_list, library_name):
        self.book_list = book_list
        self.library_name = library_name
        self.lend_record = {}
    def display_book(self):
        print(self.book_list)
    def add_book(self):
        book = input("Enter book name : ")
        self.book_list.append(book) 
    def lend_book(self):
        book=input("Enter book name").capitalize()
        if book in self.book_list:
            name = input("Enter your name : ")
            self.book_list.remove(book)   
            self.lend_record[book] = name 
        else:
            print("Invalid Input")
            print(f"Book does not exist in library.This book is taken by {self.lend_record[book]}")
    def return_book(self):
        book = input("Enter book name : ").capitalize()
        if book in self.lend_record:
            self.book_list.append(book)      
            del self.lend_record[book]
        else:
            print("Please enter valid input") 
    
        

if __name__=="__main__":
    print("Library Management System")
    book_list=["C","C++","Java","Python"]
    librarysystem=Library(book_list,'librarysystem')
    while True:
        user = input("\nD for Display book, A for Add book, L for lend book, R for return book, and Q for exit :")
        if user == "Q" or user == "q":
            break
        elif user == "display" or user == "d" or user == "D":
            librarysystem.display_book()
        elif user == "add" or user == "a" or user == "A":
            librarysystem.add_book()
        elif user == "lend" or user == "l" or user == "L":
            librarysystem.lend_book()
        elif user == "return" or user == "r" or user == "R":
           librarysystem.return_book()
