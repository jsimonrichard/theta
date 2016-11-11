import re
import random
import math

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

class shift_key(object):
    def encode(string, key):
        output = []
        key = list(str(key))
        string = clean_string(string)
        
        for i in range(len(string)):      
            index = int(letters.index( string[i] ))
            shift_amount = key[i % len(key)]
            output.append(shift( string[i], shift_amount ))
        return ''.join(output)
    
    def decode(string, key):
        output = []
        key = list(str(key))
        string = clean_string(string)
        
        for i in range(len(string)):      
            index = int(letters.index( string[i] ))
            shift_amount = -int((key[i % len(key)]))
            output.append(shift( string[i], shift_amount ))
        return ''.join(output)


class sort_key(object):
    def encode(string, key):
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

    def decode(string, key):
        output = []
        temp = []
        key = list(str(key))
        string = clean_string(string)

        comp_list = []
        decode_key = []

        for i in range(math.ceil(len(string) / len(key))):
            comp_list += key

        for i in range(len(comp_list) - len(string)):
            del comp_list[len(comp_list) - 1]

        for n in range(0, 9):
            count = comp_list.count(str(n))
            for i in range(count):
                decode_key.append(str(n))
            
        #assign
        for i in range(len(string)):      
            temp.append([string[i], decode_key[i]])

        #sort
        for i in comp_list:
            for s in range(len(temp)):
                if int(temp[s][1]) == int(i):
                    output.append(temp[s][0])
                    del temp[s]
                    break
        
        return ''.join(output)

def str_to_int(string):
    string = clean_string(string)
    output = []
    for i in string:
        output.append( int(letters.index(i)) + 1 )
    return output

def int_to_string(int_list):
    output = []
    for i in int_list:
        output.append( letters[i - 1] )
    return output

def onetime_pad(length):
    output = []
    for i in range(length):
        output.append(str(random.randint(0, 9)))
    return ''.join(output)

class algo(object):
    #These fuctions take a while to run
    def primes(key, steps):
        out = str(key)
        for i in range(steps):
            x = out[-7:-1]
            middle = math.floor(len(x)/2)
            x_firsthalf, x_secondhalf = (x[0:middle], x[middle:len(x)])
            x = int(x_firsthalf) * int(x_secondhalf)
            x = (2**x) - 1
            out += str(x)

        return out

