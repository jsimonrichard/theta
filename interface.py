import python.theta.theta as theta

def shift():
    print()
    print(' 1) Encode\n 2) Decode\n')
    command = input('Command > ')

    if command == '1':
        print('Encode\n')
        string = input('String > ')
        key = input('Key > ')
        print(theta.shift_key.encode(string, key))
    elif command == '2':
        print('Decode\n')
        string = input('String > ')
        key = input('Key > ')
        print(theta.shift_key.decode(string, key))
    else:
        print('\nCommand Not Reconized\n')
        shift()

    main()

def sort():
    print()
    print(' 1) Encode\n 2) Decode\n')
    command = input('Command > ')

    if command == '1':
        print('Encode\n')
        string = input('String > ')
        key = input('Key > ')
        print(theta.sort_key.encode(string, key))
    elif command == '2':
        print('Decode\n')
        string = input('String > ')
        key = input('Key > ')
        print(theta.sort_key.decode(string, key))
    else:
        print('\nCommand Not Reconized\n')
        sort()

    main()

def str_int():
    print()
    print(' 1) String to Int\n 2) Int to String\n')
    command = input('Command > ')

    if command == '1':
        print('String to Int\n')
        string = input('String > ')
        print(theta.str_to_int(string))
    elif command == '2':
        print('Int to String\n')
        print('Intagers must entered with commas in between. No spaces. (ex. 1,2,3,4,5)')
        string = input('Int > ')
        string = string.split(',')
        for i in range(len(string)):
            string[i] = int(string[i])
        
        print(theta.int_to_str(string))
    else:
        print('\nCommand Not Reconized\n')
        str_int()

    main()

def onetime_pad():
    print('Onetime Pad\n')
    length = int(input('Length > '))
    print(theta.onetime_pad(length))
    
    main()

def algo():
    print()
    print(' 1) Primes\n')
    command = input('Command > ')

    if command == '1':
        print('Primes (It may take several minutes to compute)\n')
        key = int(input('Key > '))
        steps = int(input('Steps > '))
        print(theta.algo.primes(key, steps))
    else:
        print('\nCommand Not Reconized\n')
        algo()

    main()

def main():
    print()
    print(' 1) Shift Key\n 2) Sort Key\n 3) Str and Int conversion\n 4) Onetime Pad\n 5) Expanding Algorithum\n')
    command = input('Command > ')

    if command == '1':
        shift()
    elif command == '2':
        sort()
    elif command == '3':
        str_int()
    elif command == '4':
        onetime_pad()
    elif command == '5':
        algo()
    else:
        print('\nCommand Not Reconized\n')
        main()


print('#############')
print('### THETA ###')
print('#############')
print('A cryptography libray.')

main()
