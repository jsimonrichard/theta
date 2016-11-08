import re
import random

letters = ['a', 'b', 'c', 'd', 'e',
           'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

def clean_string(string):
    regex = re.compile('[^a-z]')
    return regex.sub('', string)

def shift (letter, shift):
    index = int(letters.index(letter))
    return letters[ (index + int(shift)) % 26]
    
def shift_key(string, key):
    output = []
    key = list(str(key))
    string = clean_string(string)
    
    for i in range(len(string)):      
        index = int(letters.index( string[i] ))
        shift_amount = key[i % len(key)]
        output.append(shift( string[i], shift_amount ))
    return ''.join(output)

def sort_key(string, key):
    output = []
    temp = []
    key = list(str(key))
    string = clean_string(string)

    #assign
    for i in range(len(string)):      
        temp.append([string[i], key[i % len(key)]])

    #sort
    for n in range(0, 9):
        for s in temp:
            if int(s[1]) == int(n):
                output.append(s[0])

    
    
    return ''.join(output)

def str_to_int(string):
    string = clean_string(string)
    output = []
    for i in string:
        output.append( int(letters.index(i)) + 1 )
    return output
<<<<<<< HEAD

def onetime_pad(length):
    output = []
    for i in range(length):
        output.append(str(random.randint(0, 9)))
    return ''.join(output)

print(onetime_pad(100))
=======
>>>>>>> 994526cf78e626be07e66bfd527bca1dc1415616
