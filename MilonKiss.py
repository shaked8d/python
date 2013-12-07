#!/usr/bin/python

def AddWord(dict, eng_word, heb_word):
    dict[eng_word] = heb_word
    return dict

def SearchWord(dict, eng_word):
    if dict.has_key(eng_word) == True:
        print "The translation of " + eng_word + " is " + dict[eng_word]
        return True
    else:
        print "I don't have the word " + eng_word + " in me :("
        return False

def DeleteWord(dict, eng_word):
    answer = SearchWord(dict, eng_word)
    if answer == True:
        del dict[eng_word]
        print "DELETED \n"
        return dict
    else:
        return dict

def Exit():
    return 0

def GetUserEngWord():
    eng_word = raw_input("Enter Eng word: ")
    return eng_word
def GetUserHebWord():
    heb_word = raw_input("Enter Heb word: ")
    return heb_word
   
   
dict = {}
user = 0
while user != 4:
    user = raw_input("""\n Welcome! Enter what would you like to do:
        1) add a word
        2) search a word
        3) delete a word
        4) Exit the program\n""")
    print "You entered ", user + " \n"

    if user == '1':
        eng_word = GetUserEngWord()
        heb_word = GetUserHebWord()
        dict = AddWord(dict, eng_word, heb_word)
        print dict

    elif user == '2':
        eng_word = GetUserEngWord()
        SearchWord(dict, eng_word)

    elif user == '3':
        eng_word = GetUserEngWord()
        dict = DeleteWord(dict, eng_word)

    elif user == '4':
        print "Bye Bye :) \n"
        exit()

    else:
        print "You entered a wrong number. Type again \n"
