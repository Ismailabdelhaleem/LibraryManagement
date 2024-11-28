#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Library:
    def __init__(self,booksList,libraryname,lendedbooks):
        self.booksList=booksList
        self.libraryname=libraryname
        self.lendedbooks=[]
        
    def displaybooks(self):
        print(f'The available books:')
        for book in self.bookslist:
            print(f'{book}')
            
    def add_Book(self,book):
        self.booksList.append(book)
        
    def Return_Book(self,book):
        '''Parameters:BookName
        
         function doesn't have a return
         it only changes the the internal list of books and lended books 
        '''
        self.booksList.append(book)
        self.lendedbooks.remove(book)
