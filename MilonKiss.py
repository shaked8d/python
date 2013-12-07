#!/usr/bin/python

def AddWord(dict, eng_word, heb_word):
    dict[eng_word] = heb_word
    return "The word " + eng_word + "added with the trans" + heb_word

def SearchWord(dict, eng_word):
    if dict.has_key(eng_word) == True:
        return dict[eng_word]
    else:
        return "I don't have the word " + eng_word + " in me :("

def DeleteWord(dict, eng_word):
    answer = SearchWord(dict, eng_word)
    if answer == dict[eng_word]:
        del dict[eng_word]
    else:
        return "I don't have the word " + eng_word + "in me :("

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
    user = raw_input("""Welcome! Enter what would you like to do:
        1) add a word
        2) search a word
        3) delete a word
        4) Exit the program
        
        """)
    print "You entered ", user + " "
    if user == '1':
        eng_word = GetUserEngWord()
        heb_word = GetUserHebWord()
        AddWord(dict, eng_word, heb_word)
    elif user == '2':
        eng_word = GetUserEngWord()
        SearchWord(dict, eng_word)
    elif user == '3':
        eng_word = GetUserEngWord()
        DeleteWord(doct, eng_word)
    elif user == '4':
        exit()
    else:
        print "You entered a wrong number. Type again"
