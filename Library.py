#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Library:
    def __init__(self,booksList=[],libraryname='',lendedbooks={}):
        self.booksList=booksList
        self.libraryname=libraryname
        self.lendedbooks=lendedbooks

    def displaybooks(self):
        print(f'The available books:')
        for book in self.booksList:
            if not any(book in books for books in self.lendedbooks.values()):
                print(book)

    #Task 1.3
    def lend_book(self):
        user_name=input("Enter Ur Name: ")
        book_name=input("Enter Book want to lend: ")
        if book_name in self.booksList:
            if book_name in self.lendedbooks.values():
                print("sorry the book already has been lended")
            else:
                if user_name in self.lendedbooks:
                    self.lendedbooks[user_name].append(book_name)  
                else:
                    self.lendedbooks[user_name] = [book_name]
        else:
                print("Book Not Avaliable in Store")

        for user , book in self.lendedbooks.items():
            print(f"User:{user},Books_lended:{book}")

 #Task 1.4
    def Add_book(self):
        book_name=input("Enter New Book Name: ")
        if book_name in self.booksList :
            print("the Book already exist")
        else:
            self.booksList.append(book_name)

#Task 1.5
    def return_book(self):
        user_name=input("Enter Ur Name: ")
        book_name=input("Enter Book U want to Return: ")
        for user, book in self.lendedbooks.items():
            if user == user_name: 
                if book_name in book:
                    book.remove(book_name)
                    print("book has been returned")
                    print(f"User:{user},Books_lended:{book}")
                    if not  book: 
                        del self.lendedbooks[user_name]
                        return
            else:
                print(f"Book '{book_name}' not found under the user '{user_name}'.")

