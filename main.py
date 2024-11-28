#!/usr/bin/env python
# coding: utf-8

# In[3]:


from Library import Library
books = ['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS']
CodeWithHarry=Library(books,'CodeWithHarry')
while True:
    print("\nWelcome to CodeWithHarry Library")
    print("1.Display Books")
    print("2.Lend a Book")
    print("3.Add a Book")
    print("4.Return a Book")
    print("5.Exit")
    user_input=input("Enter your choice! >>")
    if user_input=='1':
        CodeWithHarry.displaybooks()
    elif user_input=='2':
        CodeWithHarry.lend_book()
    elif user_input=='3':
        CodeWithHarry.Add_book()
    elif user_input=='4':
        CodeWithHarry.return_book()
    elif user_input=='5':
        print("Thank You for using CodeWithHarry Library.")
        break
    else:
        print("Invalid Choice!\nPlease enter single number 1,2,3,4 or 5")

