#Define regular expressions to match strings that:

import re
s = ['Tartaruga',
     'Casa',
     'geografia',
     'tarantula0',
     '2024',
     'Morango',
     'Melancia',
     'melancolia',
     'olaa',
     'toto',
     'ToTo',
     '0.5',
     'hi',
     'melão',
     'Mermão',
     '345.87']

#1. have a 't'

def t (s):
    for word in s:
        if (re.findall(r't',word)) != []:
            print(word)

t(s)

#2. have a 't' or a 'T'

def t_T (s):
    for word in s:
        if (re.findall(r'[tT]',word)) != []:
            print(word)

t_T(s)

#3. have a letter (and how many)

def letter_count (s):
    for word in s:
        if (re.findall(r'[A-Za-z]',word)) != []:
            print(word, len(word))

letter_count(s)

#4. have a digit

def digit (s):
    for word in s:
        if (re.findall(r'\d',word)) != []:
            print(word)

digit(s)

#5. have a decimal number

def dec (s):
    for word in s:
        if (re.findall(r'\d+\.\d+',word)) != []:
            print(word)

dec(s)

#6. have a lenght higher than 3 characters

def characters (s):
    for word in s:
        if (re.findall(r'\w{3,}',word)) != []:
            print(word)

characters(s)

#7. have an 'M' but not an 'm'

def Mbutnotm (s):
    for word in s:
        if (re.findall(r'M',word)) != [] and (re.findall(r'm',word)) == []:
            print(word)

Mbutnotm(s)

#8. have a character repeated twice

def repeated (s):
    for word in s:
        if (re.findall(r'\b\w{2}',word)) != []:
            print(word)

repeated(s)

#9. have only one character repeated many times

#10. put all words between {}