import socket
import random

#public_key = [3, 17] # Testing

public_key = [53, 524287]
length = 6
method = None

global_host = 'localhost'
global_port = 5555


def mix(a, gen):
    out = gen**a % public_key[1]
    return out

def gen_private(length):
    start = '1'
    end = ''
    for i in range(length):
        end += '9'
    for i in range(length - 1):
        start += '0'

    start = int(start)
    end = int(end)
        
    return random.randint(start, end)


#Server/Client

def server():
    print('Starting Socket...')

    host = ''
    port = global_port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((host, port))
    except socket.error as e:
        print(str(e))

    print('Running on', host + ':' + str(port))

    s.listen(5)
    conn, addr = s.accept()

    print('Connected to', str(addr[0]) + ':' + str(addr[1]))

    return conn

def client():
    host = global_host
    port = global_port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        print('Connected to Server')
        return s
    except:
        print('Connection Failed')
        return 'ERROR'

def get_socket():
    global method
    print('S => Server\nC => Client')
    method_input = input('Method > ').upper()
    print()

    if method_input == 'S':
        s = server()
        method = 's'
        return s
    elif method_input == 'C':
        s = client()
        method = 'c'
        return s
    else:
        print('Invalid Input')
        return get_socket()

def server_action(s, private_key):
    data = s.recv(2048)
    data = data.decode('utf-8')
    reply = str(mix(private_key, public_key[0]))
    s.sendall(str.encode(reply))
    s.close()
    return data

def client_action(s, private_key):
    s.send(str(mix(private_key, public_key[0])).encode())
    data = s.recv(2048)
    reply = data.decode('utf-8')
    return reply

def set_host_port():
    print('Setting Host and Port')
    print('If you are going to run as a server,\nPort is the only value that matters.')
    host = input('Host > ')
    port = int(input('Port > '))
    return (host, port)

#Start Up

def init(defaults=False):
    global global_host, global_port
    
    if not defaults:
        global_host, global_port = set_host_port()
        print()
        
    s = get_socket()
    print()

    if method == 'c':
        input('Ready to Calculate Key <ENTER>')

    #Messages

    private = gen_private(length)

    if method == 's':
        net_mix = int(server_action(s, private))
    elif method == 'c':
        net_mix = int(client_action(s, private))

    key = mix(private, net_mix)
    return key

#INIT

def main():
    print('~~~Public Key~~~')
    print()

    key = init()
    print('Secure Key => ' + str(key))
    input()
