#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Library:
    def __init__(self,booksList,libraryname,lendedbooks):
        self.booksList=booksList
        self.libraryname=libraryname
        self.lendedbooks={}
    def displaybooks(self):
        print(f'The available books:')
        for book in self.bookslist:
            print(f'{book}')

