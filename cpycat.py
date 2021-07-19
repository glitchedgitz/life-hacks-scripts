import sys
import pyperclip
import msvcrt as m
import time

def help():
    print('''

            |  cpycat
            |
    /\_/\   |   /\_/\    
   ( -.o )  |  ( -.o )
    > ^ <   |   > ^ < 

    Copy to clipboard from pipe

    default  :   Copy line by line
    -a       :   To copy all, not line by line
    -h       :   To print this
    timeout  :   Automatic coping after timeout(sec)
                 cat urls.txt | cpycat 5
    ''')
    sys.exit(0)

def sp():
    time.sleep(timeout)

def copyallinput():
    copytext = ''
    for line in lines:
        line = line.strip()
        line = line.strip('\r')
        copytext+=line+'\n'
    pyperclip.copy(copytext)

def runit(func):
    for line in lines:
        line = line.strip()
        if line != "":
            print(line)
            pyperclip.copy(line)
            func()

timeout = 0
copyall = False

if len(sys.argv) > 1:
    if sys.argv[1] == "-a":
        copyall = True
    elif sys.argv[1]=="-h":
        help()
    else:
        timeout = int(sys.argv[1])

lines = []
for line in sys.stdin:
    lines.append(line)

if not copyall:
    if timeout == 0:
        runit(m.getch)
    else:
        runit(sp)
else:
    copyallinput()
