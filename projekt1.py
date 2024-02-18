"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Monika Jelínková
email: jelinkova.monik@seznam.cz
discord: Moňa J. mona_53888
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
user = input("Enter your user name: ")
password = input("Enter your password: ")

if user in users and password == users[user]:
    print(f"Welcome to the app, {user} \nWe have 3 texts to be analyzed")
    print("-" * 30)
    chosen_text = input("Enter a number btw. 1 and 3 to select: ")
    if int(chosen_text) in (1, 2, 3):
        pass
    elif isinstance(int(chosen_text), int):
        print("Your number is not in choice")
    else:
        print("Unkown choice, terminating the program...") #nevím jak ošetřit string variantu

    text = TEXTS[int(chosen_text) - 1]
    words = text.replace(".", "").replace(",","").split() #odstranit čárky a tečky ve větách, rozsekat na slova
    number = len(words)
    number2 = 0
    titlecase = 0
    uppercase = 0
    lowercase = 0
    is_numeric = 0
    sum = 0
    for word in words:
        number2 += 1
        if word.isupper():
            uppercase += 1
        elif word.istitle():
            titlecase += 1
        elif word.islower():
            lowercase += 1
        elif word.isdigit():
            is_numeric += 1
            sum += int(word)
    print("-" * 30)
    print(f"""There are {number} words in the selected text.
There are {titlecase} titlecase words.
There are {uppercase} uppercase words.
There are {lowercase} lowercase words.
There are {is_numeric} numeric strings.
The sum of all the numbers {sum}.""")
    print("-" * 30) 
    



else:
    print("Unregistered user, terminating the program...")
    

