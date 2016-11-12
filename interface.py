import theta
import sys
import os

def shift():
    print()
    print(' 1) Encode\n 2) Decode\n quit/exit to close the program\n')
    command = input('Command > ')

    if command == '1':
        print('Encode\n')
        string = input('String > ')
        key = input('Key > ')

        ans = theta.shift_key.encode(string, key)
        print(ans)
        log('sort:encode', ans)
        input()
        
    elif command == '2':
        print('Decode\n')
        string = input('String > ')
        key = input('Key > ')

        ans = theta.shift_key.decode(string, key)
        print(ans)
        log('sort:decode', ans)
        input()
        
    elif command == 'quit' or command == 'exit':
        sys.exit()
    else:
        print('\nCommand Not Reconized\n')
        shift()

    main()

def sort():
    print()
    print(' 1) Encode\n 2) Decode\n quit/exit to close the program\n')
    command = input('Command > ')

    if command == '1':
        print('Encode\n')
        string = input('String > ')
        key = input('Key > ')

        ans = theta.sort_key.encode(string, key)
        print(ans)
        log('sort:encode', ans)
        input()
        
    elif command == '2':
        print('Decode\n')
        string = input('String > ')
        key = input('Key > ')

        ans = theta.sort_key.decode(string, key)
        print(ans)
        log('sort:decode', ans)
        input()
        
    elif command == 'quit' or command == 'exit':
        sys.exit()
    else:
        print('\nCommand Not Reconized\n')
        sort()

    main()

def str_int():
    print()
    print(' 1) String to Int\n 2) Int to String\n quit/exit to close the program\n')
    command = input('Command > ')

    if command == '1':
        print('String to Int\n')
        string = input('String > ')
        ans = theta.str_to_int(string)
        print(ans)
        log('str_to_int', ans)
        input()
        
    elif command == '2':
        print('Int to String\n')
        print('Intagers must entered with commas in between. No spaces. (ex. 1,2,3,4,5)')
        string = input('Int > ')
        string = string.split(',')
        for i in range(len(string)):
            string[i] = int(string[i])

        ans = theta.int_to_str(string)
        print(ans)
        log('int_to_str', ans)
        input()
        
    elif command == 'quit' or command == 'exit':
        sys.exit()
    else:
        print('\nCommand Not Reconized\n')
        str_int()

    main()

def onetime_pad():
    print('Onetime Pad\n')
    length = int(input('Length > '))
    ans = theta.onetime_pad(length)
    print(ans)
    log('onetime_pad', ans)
    input()
        
    main()

def algo():
    print()
    print(' 1) Primes\n quit/exit to close the program\n')
    command = input('Command > ')

    if command == '1':
        print('Primes (It may take several minutes to compute)\n')
        key = int(input('Key > '))
        steps = int(input('Steps > '))
        ans = theta.algo.primes(key, steps)
        print(ans)
        log('expanding_algorithums:primes', ans)
        input()
        
    elif command == 'quit' or command == 'exit':
        sys.exit()
    else:
        print('\nCommand Not Reconized\n')
        algo()

    main()

def hidden_file():
    print('Hidden File (File system must be NFTS)\nFile Name must be full path.\nHidden File Name does not need any path.\nWhen this program is executed, it will open notepad.')
    print()
    file_name = input('File Name > ')
    hidden_name = input('Hidden File Name > ')
    
    try:
        os.system('notepad ' + file_name + ':' + hidden_name)
        log('hidden_file', file_name + ':' + hidden_name)
    except:
        print('Error')
    input()

    main()

def log(origin, data):
    origin, data = (str(origin), str(data))
    data = '\n -- ' + origin + ' => ' + data
    log_file = open('log.txt', 'a')
    log = log_file.write(data)
    log_file.close()

def show_log():
    print('Log\n')
    log_file = open('log.txt', 'r')
    log = log_file.read()
    log_file.close()

    if log == '':
        print('Nothing Here')
    else:
        print(log)
    input()
    
    main()

def clear_log():
    print('Clearing log...')
    log_file = open('log.txt', 'w')
    log = log_file.write('')
    log_file.close()
    print('Done')
    input()

    main()

def main():
    print('''
 1) Shift Key
 2) Sort Key
 3) Str and Int conversion
 4) Onetime Pad
 5) Expanding Algorithum
 6) Hidden File (View and Edit)
 7) View Log
 8) Clear Log
 ''')
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
    elif command == '6':
        hidden_file()
    elif command == '7':
        show_log()
    elif command == '8':
        clear_log()
    elif command == 'quit' or command == 'exit':
        sys.exit()
    elif command == 'cls' or command == 'clear':
        a = os.system('cls')
        main()
    else:
        print('\nCommand Not Reconized\n')
        main()


print('#############')
print('### THETA ###')
print('#############')
print('A cryptography libray.')

main()
