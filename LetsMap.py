#!/usr/bin/python

def func(do):
    """
    This func gets a word and transform it to operation
    We assume the operation is real
    """
    do = eval(do)
    return do

def my_map(do, list):
    """
    This func gets an operation and a list, and returns the operation on every item on the list.
    """
   
    do = func(do)
    new_list = []
    
    for i in range(len(list)):
        count = do(list[i])
        new_list.append(count)

    print new_list    
       
def Get_func():
    """
    This func gets operation (do) from user
    """
    do = raw_input("Enter an operation: ")
    return do

def Get_list():
    """
    This finc gets a list from user
    """
    list = raw_input("Enter a list: ")
    list = list.split(', ')
    return list


do = Get_func()
list = Get_list()
my_map(do, list)
